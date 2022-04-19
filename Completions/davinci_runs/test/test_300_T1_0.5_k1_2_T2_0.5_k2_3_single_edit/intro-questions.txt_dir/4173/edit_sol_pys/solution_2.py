import math


def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c!=0:
                return False
            else:
                return None
        else:
            return [-c/b]
    
    d = b*b - 4*a*c
    if d < 0:
        return False
    elif d == 0:
        return [-b/(2*a)]
    else:
        return [(-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)]


if __name__ == "__main__":
    print(solve_quadratic(0, 0, 0))
