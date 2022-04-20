

def main():
    n, x = map(int, input().split())
    xi = list(map(int, input().split()))
    xi.append(x)
    xi.sort()
    index = xi.index(x)

    if index == 0:
        print(xi[index+1]-x)
    elif index == n:
        print(x-xi[index-1])
    else:
        print(max(x-xi[index-1], xi[index+1]-x))

if __name__ == '__main__':
    main()