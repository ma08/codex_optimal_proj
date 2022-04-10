

def longest_sublist_with_same_sum(lst, start, end):
    if start == end:
        return (start, start)
    if end - start == 1:
        if lst[start] == lst[end]:
            return (start, end)
        else:
            return (start, start)

    mid = (start + end) // 2
    left_longest = longest_sublist_with_same_sum(lst, start, mid)
    right_longest = longest_sublist_with_same_sum(lst, mid+1, end)
    if left_longest[1] - left_longest[0] > right_longest[1] - right_longest[0]:
        return left_longest
    else:
        return right_longest

def main():
    n = int(input())
    lst = [int(x) for x in input().split()]
    longest = longest_sublist_with_same_sum(lst, 0, n-1)
    print(longest[0]+1, longest[1]+1)

if __name__ == "__main__":
    main()