

# Accepted after 2 submissions.
# I don't understand why my first submission failed. It's the same answer, but I guess the decimal places were different. I'll leave the first submission as it is and keep the second one.
import math

def main():
    # Read input
    triangles = []
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        triangles.append(Triangle(a, b, c))

class Triangle:
    """Represents a triangle with three sides."""

    def __init__(self, a, b, c):
        """Initializes the triangle with the three sides."""
        self._a = a
        self._b = b
        self._c = c

    def perimeter(self):
        """Returns the perimeter of the triangle."""
        return self._a + self._b + self._c

    def area(self):
        """Returns the area of the triangle."""
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

def main():
    # Read input
    triangles = []
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        triangles.append(Triangle(a, b, c))

    # Print output
    print(min_rod_length(triangles))

if __name__ == "__main__":
    main()
