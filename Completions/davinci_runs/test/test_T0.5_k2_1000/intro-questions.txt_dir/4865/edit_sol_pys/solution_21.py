

#import sys

def main():
    #lines = sys.stdin.read().splitlines() # read in the input from STDIN
    lines = ['1', 'F 60 13 20', 'B 60 13 20', 'F 60 13 20', 'B 60 13 20']
    N = int(lines[0])
    for i in range(1, N+1):
        line = lines[i].split()
        if line[0] == 'F':
            print(str(int(line[2]) + (int(line[1])//60))+' '+str(int(line[3]) + (int(line[1])%60))+' '+line[4])
        else:
            print(str(int(line[2]) - (int(line[1])//60))+' '+str(int(line[3]) - (int(line[1])%60))+' '+line[4])

if __name__ == '__main__':
    main()
