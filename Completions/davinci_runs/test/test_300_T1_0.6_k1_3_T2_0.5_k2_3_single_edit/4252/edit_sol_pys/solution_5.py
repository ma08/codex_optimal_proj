
def minRemove(name):
    res = ""
    for i in name:
        if i == "x":
            if len(res) >= 2 and res[-1] == "x" and res[-2] == "x": 
                res = res[:-2]
            else:
                res += i
        else:
            res += i
    return len(name) - len(res) 

if __name__ == "__main__":
    n = int(input())
    name = input()
    print(minRemove(name))
