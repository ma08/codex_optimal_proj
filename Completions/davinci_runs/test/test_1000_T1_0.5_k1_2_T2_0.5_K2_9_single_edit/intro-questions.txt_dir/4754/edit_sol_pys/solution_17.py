

# SOLUTION

from collections import Counter

def sock_merchant(n, ar):
    """
    John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

    For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

    Function Description

    Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

    sockMerchant has the following parameter(s):

    n: the number of socks in the pile
    ar: the colors of each sock
    Input Format

    The first line contains an integer , the number of socks represented in .
    The second line contains  space-separated integers describing the colors  of the socks in the pile.

    Constraints

    where
    Output Format

    Return the total number of matching pairs of socks that John can sell.
    """
    sock_count = Counter(ar)
    pairs_needed = 0
    for i in sock_count.values():
        pairs_needed += i // 2
    return pairs_needed


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sock_merchant(n, ar)
    print(result)
