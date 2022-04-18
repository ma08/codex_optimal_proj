
a, b, c = map(int, input().split())
order = input()

if order == "ABC":
    print(min(a, b, c), max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c))  # noqa: E501
elif order == "ACB":
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))  # noqa: E501
elif order == "BAC":
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))  # noqa: E501
elif order == "BCA":
    print(max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))  # noqa: E501
elif order == "CAB":
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))  # noqa: E501
elif order == "CBA":
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))  # noqa: E501
