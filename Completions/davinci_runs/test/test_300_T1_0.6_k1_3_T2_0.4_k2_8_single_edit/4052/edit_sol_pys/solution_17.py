

def swap(char, i, j):
    char_list = list(char)
    char_list[i], char_list[j] = char_list[j], char_list[i]
    return "".join(char_list)

def is_valid(char_list, target):
    i = 0
    while i < len(char_list):
        if char_list[i] == target[i]:
            i += 1
        else:
            j = i + 1
            while j < len(char_list) and char_list[j] != target[i]:
                j += 1
            if j == len(char_list):
                return False
            else:
                char_list = swap(char_list, i, j)
                i += 1
    return True

def can_swap(char_list, target):
    i = 0
    while i < len(char_list):
        if char_list[i] != target[i]:
            j = i + 1
            while j < len(char_list) and char_list[j] != target[i]:
                j += 1
            if j == len(char_list):
                return False
    return True

def get_swap(char_list, target):
    swaps = []
    i = 0
    while i < len(char_list):
        if char_list[i] != target[i]:
            j = i + 1
            while j < len(char_list) and char_list[j] != target[i]:
                j += 1
            if j == len(char_list):
                return False
            swaps.append(j)
            char_list = swap(char_list, i, j)
        i += 1
    return swaps

def main():
    n = int(input())
    char_list = input()
    target = input()
    if can_swap(char_list, target):
        swaps = get_swap(char_list, target)
        print(len(swaps))
        print(" ".join(map(str, swaps)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
