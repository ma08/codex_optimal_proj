
def minRemove(name):
    res = name.replace("xxx", "")
    return len(name) - len(res) - name.count("xxx")

if __name__ == "__main__":
    n = int(input())
    name = input()
    print(minRemove(name))
