from operator import itemgetter

def get_max_possible_sum(lst):
    lst.sort(key=itemgetter(1), reverse=True)
    return sum(lst[:K])

A, B, C, K = map(int, input().split())
cards = [A, B, C]
print(get_max_possible_sum(cards)[0])
