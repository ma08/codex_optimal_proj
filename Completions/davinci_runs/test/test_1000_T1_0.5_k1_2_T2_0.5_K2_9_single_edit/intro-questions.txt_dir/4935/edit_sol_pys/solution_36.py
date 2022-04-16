

def main():
    """
    Input:
    - One line containing a positive integer $N$ ($1 \le N \le 4$), the number of line segments making up the mountain, followed by a space and then a real number $g$ ($1 \le g \le 100$), the coefficient of acceleration due to gravity.
    - $N$ more lines each containing two integers $D_i$ and then $\theta_i$ ($1 \le D \le 10^4; 1 \le \theta \le 89$): the sloped distance in metres and absolute angle in degrees of this line segment from the vertical respectively. The segments are ordered from the top of the hill to its bottom.
    Output:
    Each of the $N$ lines of output should contain one real number: the velocity of a biker starting at the $i^{\text{th}}$-most segment from the top and finishing at the foot of the mountain.
    """
    from math import radians, cos, sqrt
    N, g = map(float, input().split())
    for i in range(int(N)):
        D, theta = map(int, input().split())
        print(sqrt(2*g*D*cos(radians(theta))))

if __name__ == "__main__":
    main()
