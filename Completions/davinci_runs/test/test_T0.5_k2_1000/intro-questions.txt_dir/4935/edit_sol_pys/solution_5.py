
#!/usr/bin/env python3
import math

def get_velocity(dist, angle, gravity):
    """
    Returns the velocity of an object with a given starting angle, distance,
    and gravitational acceleration.

    :param dist: The distance of the slope.
    :param angle: The angle of the slope.
    :param gravity: The gravitational acceleration.
    :return: The velocity of the object.
    """

    # Velocity is the square root of the acceleration times the distance of the slope times the sine of the angle
    velocity = math.sqrt(gravity * dist * math.sin(math.radians(angle)))

    return velocity

def main():

    # Get the number of segments and the gravitational acceleration.
    num_segments, gravity = [float(x) for x in input().split()]

    # Create a list to store the velocities.
    velocities = []

    # Get the distance and angle for each segment.
    for i in range(int(num_segments)):

        # Get the distance and angle.
        dist, angle = [int(x) for x in input().split()]

        # Get the velocity and add it to the list.
        velocities.append(get_velocity(dist, angle, gravity))

    # Print the velocities.
    for velocity in velocities:
        print(velocity)

if __name__ == '__main__':
    main()
