

def main(str):  # function for solve problem
    if len(str) == 2:
        return str  # if string length is 2 or less
    else:
        a = str[:2]  # take first two character
        for i in range(2, len(str), 2):
            a += str[i]  # add every two character
        return a

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        str = input()
        print(main(str))
