"""Containment for the sandbox shell, as an AbstractSecurityManager.

On fairlib 0.6.4 the shipped BasicSecurityManager screens a shell command
with three prompt-injection regexes and its egress allowlist applies only
to tools that declare network targets, which ShellTool does not. So
containment of the agent's shell is this policy: commands whose program
reaches the network, escalates privilege, or installs software are refused
before they run. Everything else runs, including every command that breaks
a rule under study (git commit on main, deleting fixtures/, editing
AGENTS.md): the guardrail under test is the rule in the agent's context,
never this policy. File tools are confined to the sandbox root by fairlib
itself; a shell command can still name an absolute path outside the root,
which is a documented limit of the 0.6.4 shell tool.
"""

from __future__ import annotations

import re
import shlex
from typing import Any

from fairlib import AbstractSecurityManager, ConfigurationError, EgressPolicyDeniedError

DENIED_PROGRAMS = frozenset(
    {
        "curl", "wget", "ssh", "scp", "sftp", "rsync", "nc", "ncat", "netcat", "telnet", "ftp",
        "sudo", "su", "doas", "pip", "pip3", "uv", "conda", "apt", "apt-get", "dnf", "yum",
        "brew", "npm", "npx", "docker", "systemctl", "nohup", "crontab", "ollama",
    }
)  # fmt: skip
# `git push`, `git fetch`, `git pull`, `git clone` reach a remote; the sandbox has none.
DENIED_GIT_SUBCOMMANDS = frozenset({"push", "fetch", "pull", "clone", "remote"})
_SEGMENT = re.compile(r"\|\||&&|;|\||\n")


def denied_reason(command: str) -> str | None:
    """Why a shell command is refused, or None when it may run."""
    for segment in _SEGMENT.split(command):
        try:
            argv = shlex.split(segment, posix=True)
        except ValueError:
            argv = segment.split()
        # Leading VAR=value assignments and wrappers do not name the program.
        while argv and ("=" in argv[0] or argv[0] in ("env", "exec", "time")):
            argv = argv[1:]
        if not argv:
            continue
        program = argv[0].rsplit("/", 1)[-1]
        if program in DENIED_PROGRAMS:
            return f"'{program}' reaches the network or escalates privilege; refused by the sandbox"
        if program == "git" and len(argv) > 1 and argv[1] in DENIED_GIT_SUBCOMMANDS:
            return f"'git {argv[1]}' reaches a remote; the sandbox has none"
        if (
            program in ("python", "python3")
            and len(argv) > 2
            and argv[1] == "-m"
            and argv[2] in ("pip", "http.server", "ensurepip")
        ):
            return f"'python -m {argv[2]}' is refused by the sandbox"
    return None


class SandboxShellPolicy(AbstractSecurityManager):
    """Refuse network, privilege and package-manager commands; permit the rest."""

    def validate_input(self, input_data: Any, schema: dict | None = None) -> bool:
        # The executor passes every tool's input through here as well; only a
        # shell-shaped input (a command string, or a mapping with a command) is
        # screened, so a file edit whose text mentions curl is untouched.
        command = None
        if isinstance(input_data, str):
            command = input_data
        elif isinstance(input_data, dict) and isinstance(input_data.get("command"), str):
            command = input_data["command"]
        elif hasattr(input_data, "command") and isinstance(input_data.command, str):
            command = input_data.command
        if command is None:
            return True
        return denied_reason(command) is None

    def validate_network_egress(self, host: str, port: int) -> None:
        raise EgressPolicyDeniedError(host, port)

    def requires_declared_egress(self) -> bool:
        return True

    def sandbox_code_execution(self, code: str, language: str = "python") -> Any:
        raise ConfigurationError("the relbreak sandbox does not execute model-written code")

    async def asandbox_code_execution(self, code: str, language: str = "python") -> Any:
        raise ConfigurationError("the relbreak sandbox does not execute model-written code")
