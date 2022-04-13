
#
# def main():
#     n, p = map(int, input().split())
#     times = list(map(int, input().split()))
#     times = times[p:] + times[:p]
#     max_solved = 0
#     min_penalties = 0
#     remaining = 300
#     for t in times:
#         if remaining >= t:
#             remaining -= t
#             max_solved += 1
#             min_penalties += t
#         else:
#             break
#     print(max_solved, min_penalties)
#
# if __name__ == "__main__":
#     main()
