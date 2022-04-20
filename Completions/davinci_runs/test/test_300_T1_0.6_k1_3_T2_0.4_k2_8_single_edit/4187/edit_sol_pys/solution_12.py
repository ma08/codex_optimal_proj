
def solution(n, a):
    # n: int, the number of hours per day
    # a: list of int, 0 if the ith hour in a day is working and 1 if the ith hour is resting
    # return: int, the maximal number of continuous hours during which Polycarp rests.


    # The maximal number of continuous hours during which Polycarp rests is the maximal number of consecutive ones in a
    max_consecutive_ones = 0
    curr_consecutive_ones = 0

    for i in range(n):
        if a[i] == 1:
            curr_consecutive_ones += 1
            if curr_consecutive_ones > max_consecutive_ones:
                max_consecutive_ones = curr_consecutive_ones
        else:
            curr_consecutive_ones = 0

    return max_consecutive_ones


if __name__ == "__main__":
    n = int(input())  # number of hours per day
    a = list(map(int, input().split()))  # 0 if the ith hour in a day is working, 1 if the ith hour is resting
    print(solution(n, a))
