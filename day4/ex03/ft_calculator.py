# ft_calculator.py

class calculator:
    def __init__(self, vec):
        """Initialize the calculator with a vector."""
        self.vector = vec

    def __add__(self, other):
        """Add a scalar (other) to every element of the vector."""
        self.vector = [x + other for x in self.vector]
        print(self.vector)

    def __mul__(self, other):
        """Multiply every element of the vector by a scalar (other)."""
        self.vector = [x * other for x in self.vector]
        print(self.vector)

    def __sub__(self, other):
        """Subtract a scalar (other) from every element of the vector."""
        self.vector = [x - other for x in self.vector]
        print(self.vector)

    def __truediv__(self, other):
        """Divide every element of the vector by a scalar (other).
        If other is 0, prints an error message."""
        if other == 0:
            print("Error: Division by zero")
            return
        self.vector = [x / other for x in self.vector]
        print(self.vector)
