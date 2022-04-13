

def main():
    q = int(input())
    for i in range(q):
        n,m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        count = 0
        x = a[0]
        if a != b:
            flag = True
            for j in range(n):
                if a[j] == b[0]:
                    flag = False
            if flag:
                a.append(b[0])
                count += 1
            while a != b:
                temp = x
                x = a[b[0]-1]
                a[b[0]-1] = temp
                count += 1
            print(count)
        else:
            print(0)

main()
