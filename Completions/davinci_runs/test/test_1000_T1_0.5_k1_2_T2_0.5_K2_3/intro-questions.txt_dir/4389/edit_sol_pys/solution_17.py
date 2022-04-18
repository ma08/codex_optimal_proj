
def main(b):  # function for solve problem
    if len(b) == 2:
        return b  # if string length is 2 or less
    else:
        a = b[:2]  # take first two character
        for i in range(2, len(b), 2):
            a += b[i]  # add every two character
        return a

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
