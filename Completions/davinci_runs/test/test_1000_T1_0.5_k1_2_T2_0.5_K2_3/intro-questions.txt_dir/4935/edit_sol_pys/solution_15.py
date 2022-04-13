
import math
import math

def get_velocity(distance, angle, gravity):
    """
    Returns the velocity of an object with a given starting angle, distance,
    and gravitational acceleration.

    :param distance: The distance of the slope.
    :param angle: The angle of the slope.
    :param gravity: The gravitational acceleration.
    :return: The velocity of the object.
    """

    # Velocity is the square root of the acceleration times the distance of the slope times the sine of the angle.
    velocity = math.sqrt(gravity * distance * math.sin(math.radians(angle)))
    print(distance,angle,gravity)
    return velocity
    print(velocity)
def main():

    # Get the number of segments and the gravitational acceleration.
    num_segments, gravity = [int(x) for x in input().split()]
    print(num_segments, gravity)

    # Create a list to store the velocities.
    velocities = []

    # Get the distance and angle for each segment
    for i in range(int(num_segments)):

        # Get the distance and angle.
        distance, angle = [int(x) for x in input().split()]

        # Get the velocity and add it to the list.
        velocities.append(get_velocity(distance, angle, gravity))

    # Print the velocities.
    for velocity in velocities:
        print(int(velocity))

if __name__ == '__main__':
    main()
