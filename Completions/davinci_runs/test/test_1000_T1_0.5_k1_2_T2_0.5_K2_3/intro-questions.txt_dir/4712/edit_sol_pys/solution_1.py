

def main():
    h,w = map(int,input().split())
    a = [input() for i in range(h)]
    print('#'*(w+2)) #print first line
    for i in range(h):
        print('#'+a[i]+'#') #print lines with #
    print('#'*(w+2)) #print last line

if __name__ == '__main__':





    main()
