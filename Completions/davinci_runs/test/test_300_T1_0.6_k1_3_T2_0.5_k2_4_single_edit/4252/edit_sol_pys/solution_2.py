
def minRemove(s):
    res = []
    for i in s:
        if i == "x":
            if len(res) >= 2 and res[-1] == "x" and res[-2] == "x":
                res.pop()
                res.pop()
            else:
                res.append(i)
        else:
            res.append(i)
    return len(s) - len(res)

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(minRemove(s))
