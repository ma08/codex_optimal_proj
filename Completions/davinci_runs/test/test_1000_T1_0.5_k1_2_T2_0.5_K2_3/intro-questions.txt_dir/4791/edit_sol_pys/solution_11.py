

#-----Function Definitions-----
def max_quadrilateral(sides):
    """
    Given four side lengths, returns the maximum area of any quadrilateral that can be constructed using these lengths.
    """
    # Sort the sides in descending order
    sides.sort(reverse=True)
    # Area = (s(s-a)(s-b)(s-c))^(1/2), where s = (a+b+c)/2
    s = (sides[0] + sides[1] + sides[2] + sides[3])/2
    area = (s*(s-sides[0])*(s-sides[1])*(s-sides[2])*(s-sides[3]))**(0.5)
    return area

#-----Main Program-----
sides = list(map(float, input().split()))
print(max_quadrilateral(sides))
