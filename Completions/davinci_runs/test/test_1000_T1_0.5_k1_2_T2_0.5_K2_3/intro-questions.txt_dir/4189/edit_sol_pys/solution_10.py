

def main():
    n = int(input())
    cheese = {}
    for i in range(n):
        cheese_type = input().split()
        if cheese_type[1] not in cheese:
            cheese[cheese_type[1]] = 0
        cheese[cheese_type[1]] += 1
    print(cheese["soft"] if cheese.get("soft", 0) < cheese.get("hard", 0) else cheese.get("hard", 0))

if __name__ == "__main__":
    main()
