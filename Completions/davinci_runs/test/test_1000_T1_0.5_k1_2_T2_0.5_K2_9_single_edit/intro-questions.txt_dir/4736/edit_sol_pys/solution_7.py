
def get_factorial(num):
    if num == 0 or num == 1:
        return 1
    if num == 2:
        return 2
    return num * get_factorial(num - 1)

def get_n_choose_k(n, k):
    return get_factorial(n) // (get_factorial(k) * get_factorial(n - k))

def get_num_ways(cards, k):
    num_ways = 0
    for i in range(k):
        num_ways += cards[i] * get_n_choose_k(sum(cards) - cards[i], k - i - 1)
    return num_ways

if __name__ == "__main__":
    cards = [int(i) for i in input().split()]
    k = int(input())
    print(get_num_ways(cards, k))
