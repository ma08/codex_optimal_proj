
def main():
    string = input() #input
    stack = []
    for c in string: #iterate through string
        if c == '<': #if it is a backspace
            stack.pop() #pop last element
        else:
            stack.append(c) #append to end of list
    print(''.join(stack))

main()
