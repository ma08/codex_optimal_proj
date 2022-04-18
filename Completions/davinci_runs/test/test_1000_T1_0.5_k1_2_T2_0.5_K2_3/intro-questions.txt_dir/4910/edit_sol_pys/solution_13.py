# import sys

# N = int(sys.stdin.readline())
# costumes = set()
# for _ in range(N):
#     costumes.add(sys.stdin.readline().strip())

# costumes = list(costumes)
# costumes.sort()
# for costume in costumes:
#     print(costume)


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
