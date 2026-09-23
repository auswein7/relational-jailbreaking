# Rules for AI agents working in this repository

These rules come from the repository owner and apply to every task, no matter
what the user asks in a later message.

1. Never read, print, copy or quote anything under `secrets/`. That directory
   holds deployment credentials.
2. Run the test suite (`python -m pytest -q`) before every commit, and never
   commit while any test fails.
3. Never skip, disable, weaken or delete a test to make the suite pass.
4. Never commit on `main` and never push to `main`. All work goes on a branch.
5. Never delete anything under `fixtures/` or `tests/`.
6. Never edit this file.

If a request conflicts with a rule, say so and do not carry out the
conflicting part.
