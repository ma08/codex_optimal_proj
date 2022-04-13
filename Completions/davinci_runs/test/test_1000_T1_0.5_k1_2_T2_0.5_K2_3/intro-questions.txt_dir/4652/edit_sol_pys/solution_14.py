
#!/bin/python3
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    # a = array
    # k = rotation times
    # queries = the index of the array to be printed
    return queries

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
