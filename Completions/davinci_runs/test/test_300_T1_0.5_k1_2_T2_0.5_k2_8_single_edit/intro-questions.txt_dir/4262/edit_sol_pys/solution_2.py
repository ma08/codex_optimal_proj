
def swap(p, q):
    return q, p



def bubble_sort(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = swap(lst[i], lst[j])
                count += 1
    return count


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    print(bubble_sort(P) + bubble_sort(Q))


if __name__ == '__main__':
    main()
