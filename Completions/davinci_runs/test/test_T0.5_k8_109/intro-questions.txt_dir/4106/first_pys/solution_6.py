

from typing import List

def max_beauty_sum(n: int, k: int, x: int, a: List[int]) -> int:
    """Return the maximum possible sum of values of reposted pictures if Vova follows conditions described in the problem statement.

    :param n: the number of pictures in the news feed
    :param k: the minimum length of segment with at least one repost in it
    :param x: the number of pictures Vova is ready to repost
    :param a: the beauty of the pictures
    """
    min_beauty = min(a)
    if x < k or a.count(min_beauty) < x:
        return -1
    if k == 1:
        return sum(a)
    beauty_sum = 0
    for i in range(n):
        if a[i] == min_beauty:
            beauty_sum += min_beauty
            x -= 1
            if x == 0:
                break
    return beauty_sum


if __name__ == "__main__":
    n, k, x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    print(max_beauty_sum(n, k, x, a))