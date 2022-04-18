
def main():
    n = int(input())
    keywords = [input().lower().replace("-", " ") for _ in range(n)]
    print(len(set(keywords))

if __name__ == "__main__":
    main()
