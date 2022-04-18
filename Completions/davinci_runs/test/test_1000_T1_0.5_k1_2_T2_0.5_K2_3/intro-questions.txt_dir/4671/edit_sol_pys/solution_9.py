

def wrapper(f):
    def fun(ls):
        # complete the function
        for i in range(len(ls)):
            if ls[i][0]=="0":
                ls[i]="+91 "+ls[i][1:4]+" "+ls[i][4:9]+" "+ls[i][9:]
            elif ls[i][0]=="+":
                ls[i]="+91 "+ls[i][4:9]+" "+ls[i][9:14]+" "+ls[i][14:]
            else:
                ls[i]="+91 "+ls[i][0:5]+" "+ls[i][5:10]+" "+ls[i][10:]
        return f(ls)
    return fun

@wrapper
def sort_phone(ls):
    print(*sorted(ls), sep='\n')

if __name__ == '__main__':
    ls = [input() for _ in range(int(input()))]
    sort_phone(ls)
