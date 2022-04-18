

def main():
    n = int(input().strip())
    keywords = []
    for _ in range(n):
        keywords.append(input().strip().lower().replace("-", " "))
    print(len(set(keywords)))

if __name__ == "__main__":
    main()
