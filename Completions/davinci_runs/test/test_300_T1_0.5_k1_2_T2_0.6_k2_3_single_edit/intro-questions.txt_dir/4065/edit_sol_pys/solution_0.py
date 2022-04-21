#
# n = int(input())
# a = [int(x) for x in input().split()]
#
# contests = []
#
# for i in range(n):
#     for j in range(i+1, n):
#         if a[j] > a[i] * 2:
#             break
#         contests.append((a[i], a[j]))
#
# contests.sort()
#
# max_len = 0
# max_contest = None
#
# for i in range(len(contests)):
#     this_contest = [contests[i]]
#     for j in range(i+1, len(contests)):
#         if contests[j][0] > this_contest[-1][1] * 2:
#             break
#         this_contest.append(contests[j])
#     if len(this_contest) > max_len:
#         max_len = len(this_contest)
#         max_contest = this_contest
#
# print(max_len)



def find_max_contest(contest_list):
    max_len = 0
    max_contest = None

    for i in range(len(contest_list)):
        this_contest = [contest_list[i]]
        for j in range(i + 1, len(contest_list)):
            if contest_list[j][0] > this_contest[-1][1] * 2:
                break
            this_contest.append(contest_list[j])
        if len(this_contest) > max_len:
            max_len = len(this_contest)
            max_contest = this_contest

    return max_contest


def find_contest(contest_list, i):
    contest = [contest_list[i]]
    for j in range(i + 1, len(contest_list)):
        if contest_list[j][0] > contest[-1][1] * 2:
            break
        contest.append(contest_list[j])
    return contest


def find_contest_recursive(contest_list, i):
    if i == len(contest_list):
        return []
    this_contest = find_contest(contest_list, i)
    next_contest = find_contest_recursive(contest_list, i + len(this_contest))
    if len(this_contest) > len(next_contest):
        return this_contest
    else:
        return next_contest


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    contests = []

    for i in range(n):
        for j in range(i + 1, n):
            if a[j] > a[i] * 2:
                break
            contests.append((a[i], a[j]))

    contests.sort()

    res = find_max_contest(contests)

    print(len(res))


if __name__ == '__main__':
    main()
