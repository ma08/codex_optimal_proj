

def main():
    k = int(input())
    i = 1
    while True:
        if int(str(7)*i) % k == 0:
            print(i)
            break
        i += 1

if __name__ == '__main__':
    main()