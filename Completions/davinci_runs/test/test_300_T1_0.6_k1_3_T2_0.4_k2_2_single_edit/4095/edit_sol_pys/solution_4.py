

def build_sorted_list(n):
    sorted_list = [None] * (n + 1)
    for i in range(1, n + 1):
        sorted_list[i] = i
    return sorted_list

def count_pairs(p):
    n = len(p)
    sorted_list = build_sorted_list(n)
    same_elements_count = [0] * (n + 1)
    pairs = 0

    for i in range(n):
        current_element = p[i]
        sorted_list_position = sorted_list[current_element]
        pairs += (i + 1 - same_elements_count[sorted_list_position - 1]) * (same_elements_count[sorted_list_position + 1] if sorted_list_position < n else 0)
        sorted_list[sorted_list_position] = sorted_list_position - same_elements_count[sorted_list_position - 1] - 1

        same_elements_count[sorted_list_position - 1] += 1
        if sorted_list_position < n:
            same_elements_count[sorted_list_position + 1] -= 1

    return pairs

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    print(count_pairs(p))

if __name__ == '__main__':
    main()
