import sys
import string

n = int(sys.stdin.readline())
alphabet = string.ascii_lowercase


def main():
    for i in range(n - 1):
        line1 = sys.stdin.readline().lower()
        line2 = sys.stdin.readline().lower()

        if line1.find("pink") != -1:
            print("YES")
            break
        elif line2.find("pink") != -1:
            print("YES")
            break
        elif line1.find("rose") != -1:
            print("YES")
            break
        elif line2.find("rose") != -1:
            print("YES")
            break
        else:
            if i == n - 2:
                print("NO")

    else:
        print("NO")


if __name__ == "__main__":
    main()
