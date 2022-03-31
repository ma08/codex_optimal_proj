
def main():
    n = int(input())
    text = input().split()
    print(solve(n, text))

def solve(n, text):
    # O(n^2) brute force
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if text[i] == text[j]:
    #             return len(text[:i]) + len(text[j+1:]) + 2

    # O(n^2)
    # text = ' '.join(text)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if text[i] == text[j]:
    #             return len(text[:i]) + len(text[j+1:]) + 2

    # O(n^2)
    # text = ' '.join(text)
    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         if text[i:j] in text[j:]:
    #             return len(text[:i]) + len(text[j+len(text[i:j]):]) + 2

    # O(n^2)
    text = ' '.join(text)
    for i in range(n-1):
        for j in range(i+1, n):
            if text[i:j] in text[j:]:
                return len(text[:i]) + len(text[j+len(text[i:j]):]) + 2
    return len(text)

if __name__ == '__main__':
    main()
