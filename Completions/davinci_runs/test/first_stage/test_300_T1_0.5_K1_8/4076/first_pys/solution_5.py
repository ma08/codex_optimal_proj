

import math

def main():
    # Get user input
    A, B, H, M = map(int, input().split())

    # Calculate theta of the two hands
    theta_h = H * 30 + M * 0.5
    theta_m = M * 6

    # Calculate the length of the two hands
    length_h = A * math.cos(math.radians(theta_h))
    length_m = B * math.cos(math.radians(theta_m))

    # Calculate the distance between the two hands
    distance = math.sqrt(length_h ** 2 + length_m ** 2 - 2 * length_h * length_m * math.cos(math.radians(theta_h - theta_m)))

    # Print the answer
    print(distance)

if __name__ == '__main__':
    main()