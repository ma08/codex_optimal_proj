#include <iostream>

#include <sys>

def main():
    string line = sys.stdin.readline() 
    string d, t, s = line.split()
    d = int(d)
    t = int(t)
    s = int(s)
    if (d / s) <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
