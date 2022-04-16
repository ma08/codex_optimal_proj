
#!/usr/bin/env python
import sys,time
def main():
    f = open(sys.argv[1],'r')
    for line in f:
        print line
    f.close()
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
