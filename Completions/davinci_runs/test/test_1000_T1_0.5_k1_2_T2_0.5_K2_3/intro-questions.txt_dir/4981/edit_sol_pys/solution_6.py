
a, b, c = map(int, input().split())
order = input()

if order == "ABC":
    print(min(a, b, c), max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c))  # ABC
elif order == "ACB":
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))  # ACB
elif order == "BAC":
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))  # BAC
elif order == "BCA":
    print(max(a, b, c) - min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))  # BCA
elif order == "CAB":
    print(min(a, b, c), max(a, b, c) - min(a, b, c), min(a, b, c))  # CAB
elif order == "CBA":
    print(max(a, b, c) - min(a, b, c), min(a, b, c), max(a, b, c) - min(a, b, c))  # CBA
