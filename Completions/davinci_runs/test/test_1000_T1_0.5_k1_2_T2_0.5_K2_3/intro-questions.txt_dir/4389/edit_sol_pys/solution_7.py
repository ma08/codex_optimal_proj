

def main(a):  # function for solve problem
    if len(a) == 2:
        return a  # if string length is 2 or less
    else:
        b = a[:2]  # take first two character
        for i in range(2, len(a), 2):
            b += a[i]  # add every two character
        return b

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        b = input()
        print(main(b))
