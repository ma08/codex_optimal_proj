

def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l]) #add +91 to the number and put a space after the country code and after the local area code
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n') #print the list in sorted order

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
