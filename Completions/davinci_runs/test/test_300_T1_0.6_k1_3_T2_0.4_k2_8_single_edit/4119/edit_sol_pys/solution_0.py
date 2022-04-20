

def main():
    n, m = map(int, input().split())  # n: 人数, m: 投票数
    votes = list(map(int, input().split()))  # 投票数
    votes.sort()
    # print(n, m, votes)

    # 投票数が異なる人数
    diff_votes = len(set(votes))
    # print(diff_votes)

    # 同じ投票数が何人いるか
    same_votes = {}
    for vote in votes:
        if vote in same_votes:
            same_votes[vote] += 1
        else:
            same_votes[vote] = 1
    # print(same_votes)

    # 投票数が異なる人数が1人の場合
    if diff_votes == 1:
        print(0)
    # 投票数が異なる人数が2人の場合
    elif diff_votes == 2:
        print(min(same_votes.values()))
    # 投票数が異なる人数が3人以上の場合
    else:
        print(sum(same_votes.values()) - max(same_votes.values()))


if __name__ == '__main__':
    main()
