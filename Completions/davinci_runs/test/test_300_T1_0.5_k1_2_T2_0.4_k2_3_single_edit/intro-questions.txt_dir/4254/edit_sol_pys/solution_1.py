
import sys

def main():
    sheep, wolves = map(int, input().split())
    print("unsafe" if sheep < wolves else "safe")

if __name__ == '__main__':
    main()
