
def main():
    f = open("file.txt")
    lines = f.read().splitlines() # read in the input from STDIN
    #lines = ['1', 'F 60 13 20']
    N = int(lines[0])
    for i in range(1, N+1):
        line = lines[i].split()
        if line[0] == 'F':
            print(str(int(line[2]) + (int(line[1])//60))+' '+str(int(line[3]) + (int(line[1])%60)))
        else:
            print(str(int(line[2]) - (int(line[1])//60))+' '+str(int(line[3]) - (int(line[1])%60)))

def main():
    #main()
if __name__ == '__main__':
    main()
