

import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = {}
    for i in range(m):
        a, b = sys.stdin.readline().split()
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
    for i in range(n):
        a, b = sys.stdin.readline().split()
        a = list(a)  # ['a', 'b']
        b = list(b)  # ['c', 'd']
        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] in d:
                    if b[i] in d[a[i]]:
                        continue
                    else:
                        print("no")  # no
                        break  # break
                else:
                    print("no")  # no
                    break  # break
            else:
                print("yes")  # yes
        else:
            for i in range(len(a)):
                if a[i] in d:
                    if b[i] in d[a[i]]:
                        continue
                    else:
                        print("no")  # no
                        break  # break
                else:
                    print("no")  # no
                    break  # break
            else:
                print("yes")  # yes
            for i in range(len(b)):
                if b[i] in d:
                    if a[i] in d[b[i]]:
                        continue
                    else:
                        print("no")  # no
                        break  # break
                else:
                    print("no")  # no
                    break  # break
            else:
                print("yes")  # yes
            for i in range(len(a)):
                if a[i] in d:
                    if b[i] in d[a[i]]:
                    continue
                else:
                    print("no")  # no
                    break  # break
            else:
                print("no")  # no
                break  # break

main()
