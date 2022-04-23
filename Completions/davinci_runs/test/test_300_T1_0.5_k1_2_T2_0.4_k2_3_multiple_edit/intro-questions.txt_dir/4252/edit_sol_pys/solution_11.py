

def get_result(n, s):
    return len(s) - max(s.count("xxx"), 0)

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
