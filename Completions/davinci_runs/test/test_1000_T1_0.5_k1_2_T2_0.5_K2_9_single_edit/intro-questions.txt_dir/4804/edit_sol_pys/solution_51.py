from math import sqrt



def main():
    S = int(input())
    for i in range(2, int(sqrt(S)) + 1):
        if S % i == 0 and S // i <= 60:
            print("{}:{:02d}:{:02d}".format(S//60, i, S//i - i))

if __name__ == "__main__":
    main()
