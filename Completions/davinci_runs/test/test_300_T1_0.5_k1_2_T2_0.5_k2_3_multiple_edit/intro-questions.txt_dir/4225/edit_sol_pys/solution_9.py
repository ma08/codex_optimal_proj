

from operator import itemgetter

def get_max_possible_sum(files):
    files.sort(key=itemgetter(1), reverse=True)
    return sum(file[1] for file in files[:3])

A, B, C = map(int, input().split())
files = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(files))
