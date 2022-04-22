
def main():
    for _ in range(int(input())):
        n = int(input())
        a = []
        for _ in range(n):
            a.append(int(input()))

        ans = []

        for i in range(n):
            if i == 0:
                ans.append(a[i])
            else:
                ans.append(a[i] ^ ans[-1])

        for i in range(n):
            print(ans[i])

        if int(input()) != -1:
            raise Exception('Wrong Answer')

if __name__ == '__main__':
    main()
