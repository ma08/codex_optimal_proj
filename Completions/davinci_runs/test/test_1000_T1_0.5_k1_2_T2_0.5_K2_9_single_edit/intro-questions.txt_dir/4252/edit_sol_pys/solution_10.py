

def get_result(n, s):
    return len("".join(s.split("xxx")))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
