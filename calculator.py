class Calculator:
    def add(self, a, b):
        """Returns the sum of a and b."""
        return a + b

    def sub(self, a, b):
        """Returns the difference between a and b."""
        return a - b

    def mul(self, a, b):
        """Returns the product of a and b."""
        return a * b

    def div(self, a, b):
        """Returns the quotient of a divided by b.
        Raises a ZeroDivisionError if b is 0.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    def power(self, a, b):
        """Returns a raised to the power of b."""
        return a ** b