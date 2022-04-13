

def wrapper(f):
    def fun(ls):
        # complete the function
        for i in range(len(numbers)):
            if numbers[i][0]=="0":
                numbers[i]="+91 "+numbers[i][1:4]+" "+numbers[i][4:]
            elif numbers[i][0]=="+":
                numbers[i]="+91 "+numbers[i][4:9]+" "+numbers[i][9:]
            else:
                numbers[i]="+91 "+numbers[i][0:5]+" "+numbers[i][5:]
        return f(ls)
    return fun

@wrapper
def sort_phone(ls):
    print(*sorted(ls), sep='\n')

if __name__ == '__main__':
    ls = [input() for _ in range(int(input()))]
    sort_phone(ls)
