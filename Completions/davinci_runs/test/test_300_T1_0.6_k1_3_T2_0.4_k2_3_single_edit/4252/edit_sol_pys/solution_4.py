
def minRemove(name):
    res = []
    for i in name:
        if i == "x":
            if len(res) >= 2 and res[-1] == "x" and res[-2] == "x":
                res.pop()
                res.pop()
            else:
                res.append(i)
        else:
            res.append(i)
    return len(name) - len(res) 

if __name__ == "__main__":
    n = int(input())
    name = input() 
    print(minRemove(name))
