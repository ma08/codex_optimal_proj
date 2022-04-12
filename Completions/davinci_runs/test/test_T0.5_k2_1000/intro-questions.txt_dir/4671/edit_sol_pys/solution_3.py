

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            if l[i][0] == "0":
                l[i] = "+91 " + l[i][1:4] + " " + l[i][4:]
            elif l[i][0] == "+":
                l[i] = "+91 " + l[i][4:9] + " " + l[i][9:]
            else:
                l[i] = "+91 " + l[i][0:5] + " " + l[i][5:]
        return f(l)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
