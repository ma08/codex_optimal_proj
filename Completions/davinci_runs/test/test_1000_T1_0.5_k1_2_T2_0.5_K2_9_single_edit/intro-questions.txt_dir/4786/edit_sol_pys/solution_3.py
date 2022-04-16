

def main():
    n = int(input())
    keywords = set()
    for _ in range(n):
        keywords.add(input().lower().replace("-", " "))
    print(len(keywords))

if __name__ == "__main__":
    main()
