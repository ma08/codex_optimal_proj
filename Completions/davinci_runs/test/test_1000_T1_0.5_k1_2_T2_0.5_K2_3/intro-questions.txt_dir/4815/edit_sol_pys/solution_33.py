

def main():
    n, p, m = [int(x) for x in input().split()]
    names = [input() for _ in range(n)]
    scores = {name: 0 for name in names}
    for _ in range(m):
        name, score = input().split()
        scores[name] += int(score)  # scores[name] = scores[name] + int(score)
        if scores[name] >= p:  # if scores[name] is greater than or equal to p
            print(name, "wins!")
            return
    print("No winners!")

if __name__ == '__main__':


# def main():
#     n, p, m = [int(x) for x in input().split()]
#     names = [input() for _ in range(n)]
#     scores = {name: 0 for name in names}
#     for _ in range(m):
#         name, score = input().split()
#         scores[name] += int(score)  # scores[name] = scores[name] + int(score)
#         if scores[name] >= p:  # if scores[name] is greater than or equal to p
#             print(name, "wins!")
#             return
#     print("No winners!")
#
# if __name__ == '__main__':
#     main()
    main()
