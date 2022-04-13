
def main():
    H,W = map(int,input().split())
    a = [input() for i in range(H)]
    print('#'*(W+2))
    for i in range(H):
        print('#'+a[i]+'#')
    print('#'*(W+2))

if __name__ == '__main__':
    main()
