

from operator import itemgetter

def get_max_possible_sum(files):
    files.sort(key=itemgetter(1), reverse=True)
    return sum(files[1] for files in files[:K])

A, B, C, K = map(int, input().split())
files = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(files))
