

def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l]) # c[-10:-5] is the first 5 digits of the phone number and c[-5:] is the last 4 digits of the phone number
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n') # print the sorted list

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))] # take the number of inputs and input the phone numbers
    sort_phone(l)
