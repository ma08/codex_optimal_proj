import math

a, b, h, m = map(int, input().split())  # Read input

angle = abs(h * 30 + m * 0.5 - m * 6)  # Calculate the angle between the hands

distance = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))  # Calculate the distance

print(distance)  # Print the result
