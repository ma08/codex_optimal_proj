

def main(n, d_list):
    result = [1]
    for i in d_list:
        result.insert(i, len(result) + 1)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    n = int(input())
    d_list = list(map(int, input().split(" ")))
    main(n, d_list)
