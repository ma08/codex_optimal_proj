
# SOLUTION
import sys

class Query:
    def __init__(self):
        self.k = 0
        self.n = 0
        self.a = 0
        self.b = 0
def read_queries():
    q = int(input())
    queries = []
    for _ in range(q):
        query = Query()
        query.k, query.n, query.a, query.b = map(int, input().split())
        queries.append(query)
    return queries
def write_responses(result):
    print('\n'.join(map(str, result)))
def solve_query(query):
    k = query.k
    n = query.n
    a = query.a
    b = query.b
    if k < n*b:
        return -1
    if k < n*a:
        return 0
    k -= n*a
    return n - k//(a-b)

def solve(queries):
    result = []
    for query in queries:
        result.append(solve_query(query))
    return result

if __name__ == '__main__':
    write_responses(solve(read_queries()))
