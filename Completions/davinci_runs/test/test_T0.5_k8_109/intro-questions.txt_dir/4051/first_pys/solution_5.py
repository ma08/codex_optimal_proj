

n = int(input())
a = list(map(int, input().split()))

if a[0] < a[1]:
    for i in range(1, n-1):
        if a[i] < a[i+1]:
            continue
        elif a[i] == a[i+1]:
            if a[i] <= a[i-1]:
                continue
            else:
                print("NO")
                break
        elif a[i] - a[i+1] == 1 and a[i] >= a[i-1]:
            continue
        elif a[i] - a[i+1] > 1:
            print("NO")
            break
    else:
        print("YES")
elif a[0] > a[1]:
    for i in range(1, n-1):
        if a[i] > a[i+1]:
            continue
        elif a[i] == a[i+1]:
            if a[i] >= a[i-1]:
                continue
            else:
                print("NO")
                break
        elif a[i+1] - a[i] == 1 and a[i] <= a[i-1]:
            continue
        elif a[i+1] - a[i] > 1:
            print("NO")
            break
    else:
        print("YES")
else:
    for i in range(1, n-1):
        if a[i] == a[i+1]:
            if a[i] == a[i-1]:
                continue
            else:
                print("NO")
                break
        elif a[i] < a[i+1]:
            for j in range(i+1, n-1):
                if a[j] < a[j+1]:
                    continue
                elif a[j] == a[j+1]:
                    if a[j] <= a[j-1]:
                        continue
                    else:
                        print("NO")
                        break
                elif a[j] - a[j+1] == 1 and a[j] >= a[j-1]:
                    continue
                elif a[j] - a[j+1] > 1:
                    print("NO")
                    break
            else:
                print("YES")
            break
        elif a[i] > a[i+1]:
            for j in range(i+1, n-1):
                if a[j] > a[j+1]:
                    continue
                elif a[j] == a[j+1]:
                    if a[j] >= a[j-1]:
                        continue
                    else:
                        print("NO")
                        break
                elif a[j+1] - a[j] == 1 and a[j] <= a[j-1]:
                    continue
                elif a[j+1] - a[j] > 1:
                    print("NO")
                    break
            else:
                print("YES")
            break
        else:
            print("NO")
            break
    else:
        print("YES")