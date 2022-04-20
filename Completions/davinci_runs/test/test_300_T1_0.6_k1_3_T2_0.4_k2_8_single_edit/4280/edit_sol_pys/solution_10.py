import sys


    sys.setrecursionlimit(10000)
def main():
    n, k = map(int, raw_input().split())
    edges = [map(int, raw_input().split()) for i in range(n-1)]
    print(n, k)
    print(edges)
    # counts = {}
    # for i in edges.keys():
    #     counts[i] = len(edges[i])
    # r = 0
    # while counts:
    #     r += 1
    #     for i in counts.keys():
    #         if counts[i] == 1:
    #             del counts[i]
    #             break
    #         else:
    #             counts[i] -= 1
    # print(r)
    # print(" ".join([str(i%r+1) for i in range(n-1)]))


if __name__ == "__main__":
    main()
