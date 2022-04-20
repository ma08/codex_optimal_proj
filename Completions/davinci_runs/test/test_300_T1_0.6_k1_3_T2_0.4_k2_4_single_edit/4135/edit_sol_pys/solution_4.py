
def main():
    n = int(input())
    s = input()
    t = ''
    for i in range(n, 0, -1):
        if n%i == 0:
            for j in range(i):
                t += s[j::i][::-1]
            s = t
    print(t)



if __name__ == '__main__':
    main()
