

def get_triangle_area(a, b, c):
    """
    The area of a triangle can be calculated using Heron's formula:
    Area = sqrt(s*(s-a)*(s-b)*(s-c))
    where s = (a+b+c)/2
    """
    s = (a+b+c)/2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(int(get_triangle_area(a, b, c)))