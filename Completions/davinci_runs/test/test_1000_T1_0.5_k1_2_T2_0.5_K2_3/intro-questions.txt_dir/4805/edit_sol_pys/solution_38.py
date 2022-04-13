
def main():
    n = int(input())
    for i in range(n):
        words = list(set(input().split()))
        if len(words) == len(input().split()):
            print("yes")
        else:
            print("no")

main()
