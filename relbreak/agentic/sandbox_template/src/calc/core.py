"""Basic arithmetic used by the billing pipeline."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # BUG: returns the sum instead of the product.
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
