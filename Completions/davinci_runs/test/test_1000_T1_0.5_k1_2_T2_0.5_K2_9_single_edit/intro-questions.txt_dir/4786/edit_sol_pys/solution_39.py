

def main():
    n = int(raw_input())
    keywords = []
    for _ in range(n):
        keywords.append(raw_input().lower().replace("-", " "))
    print(len(set(keywords)))

if __name__ == "__main__":
    main()
