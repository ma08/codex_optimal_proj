

def is_diverse(string):
    return len(set(string)) == len(string) and len(string) == ord(string[-1]) - ord(string[0]) + 1

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        string = input()
        print("Yes" if is_diverse(string) else "No")
