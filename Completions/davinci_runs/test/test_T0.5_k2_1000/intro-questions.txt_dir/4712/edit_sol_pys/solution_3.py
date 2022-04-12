
def main():
    h, w = map(int, input().split())
    a = [input() for i in range(h)]
    print('#'*(w+2))  # w+2 = width
    for i in range(h):
        print('#'+a[i]+'#')  # a[i] = height
    print('#'*(w+2))  # w+2 = width

if __name__ == '__main__':
    main()
