

def main():
    n = int(input())
    keywords = []
    for _ in range(n):
        keywords.append(input().lower().replace("-", " "))
    print(len(set(keywords)))

if __name__ == "__main__":
    main()