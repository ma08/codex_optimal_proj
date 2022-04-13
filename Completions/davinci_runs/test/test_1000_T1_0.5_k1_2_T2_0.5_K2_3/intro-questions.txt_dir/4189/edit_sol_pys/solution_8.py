

def main():
    n = int(input())
    cheese = {}
    for i in range(n):
        cheese_type = input().split()
        if cheese_type[1] not in cheese:
            cheese[cheese_type[1]] = 0
        cheese[cheese_type[1]] += int(cheese_type[0])
    print(cheese["soft"] if cheese["soft"] < cheese["hard"] else cheese["hard"])

if __name__ == "__main__":
    main()
