

def minRemove(s):
    r = []
    for i in s:
        if i == "x":
            if len(r) >= 2 and r[-1] == "x" and r[-2] == "x":
                r.pop()
                r.pop()
        else:
            r.append(i)
    return len(s) - len(r)

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(minRemove(s))
