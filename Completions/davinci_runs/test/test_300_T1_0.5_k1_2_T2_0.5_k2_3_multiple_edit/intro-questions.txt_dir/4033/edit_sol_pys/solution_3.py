
# def solve():
#     a, b = map(int, input().split())

#     if a == b:
#         print(4*a)
#         return

#     if a < b:
#         a, b = b, a

#     # a > b
#     if (a+b) % 3 == 0:
#         print(2*(a+b)//3)
#     else:
#         print(2*(a+b)//3+1)


# if __name__ == "__main__":
#     solve()

from fractions import gcd


def solve():
    a, b = map(int, input().split())    

    g = gcd(a, b)
    a //= g
    b //= g

    print(a*b*2)


if __name__ == "__main__":
    solve()
