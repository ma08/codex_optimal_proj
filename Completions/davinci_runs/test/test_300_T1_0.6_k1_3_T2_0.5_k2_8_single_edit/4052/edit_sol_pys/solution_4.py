
def swap(char, i, j):
    char = list(char)
    char[i], char[j] = char[j], char[i]
    return "".join(char)

def is_valid(char, target):
    i = 0
    while i < len(char):
        if char[i] == target[i]:
            i += 1
        else:
            j = i + 1
            while j < len(char) and char[j] != target[i]:
                j += 1
            if j == len(char):
                return False
            else:
                char = swap(char, i, j)
                i += 1
    return True

def can_swap(char, target):
    i = 0
    while i < len(char):
        if char[i] != target[i]:
            j = i + 1
            while j < len(char) and char[j] != target[i]:
                j += 1
            if j == len(char):
                return False
            else:
                char = swap(char, i, j)
                i += 1
    return True

def get_swap(char, target):
    swaps = []
    i = 0
    while i < len(char):
        if char[i] != target[i]:
            j = i + 1
            while j < len(char) and char[j] != target[i]:
                j += 1
            if j == len(char):
                return False
            swaps.append(j)
            char = swap(char, i, j)
        i += 1
    return swaps

def main():
    n = int(input())
    char = input()
    target = input()
    if can_swap(char, target):
        swaps = get_swap(char, target)
        print(len(swaps))
        print(" ".join(map(str, swaps)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
