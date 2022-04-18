

def get_input():
    n = int(input())
    s = [int(input()) for i in range(n)]
    return n, s

def calculate_max_score(n, s):
    max_score = 0
    for i in range(n):
        for j in range(i+1, n+1):
            score = sum(s[i:j])
            if score % 10 != 0 and score > max_score:
                max_score = score
    return max_score

def main():
    n, s = get_input()
    max_score = calculate_max_score(n, s)
    print(max_score)

if __name__ == "__main__":
    main()
