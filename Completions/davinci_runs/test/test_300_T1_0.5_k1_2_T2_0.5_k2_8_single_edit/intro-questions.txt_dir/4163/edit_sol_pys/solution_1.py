

def main():
    a, b = map(int, input().split())
    ans = "Impossible"
    for i in range(1, 4):
        if a * b * i % 2 == 1:
            ans = "Possible"
        else:
            pass
        if ans == "Possible":
            print(ans)
            break
    else:
        print(ans)

if __name__ == '__main__':
    main()
