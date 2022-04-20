

def main():
    n = int(input())
    prefixes = set()
    suffixes = set()
    for _ in range(n-1):
        prefixes.add(input())
    for _ in range(n-1):
        suffixes.add(input())
    answer = ""
    for i in range(2*n-2):
        if prefixes:
            answer += "P"
            prefixes.remove(prefixes.pop())
        else:
            answer += "S"
            suffixes.remove(suffixes.pop())
    print(answer)

if __name__ == "__main__":
    main()