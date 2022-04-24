

def minRemove(name):
    res = 0
    for i in range(1, len(name)):
        if name[i] == "x" and name[i-1] == "x":
            res += 1
    return res

if __name__ == "__main__":
    n = int(input())
    name = input()
    print(minRemove(name))
