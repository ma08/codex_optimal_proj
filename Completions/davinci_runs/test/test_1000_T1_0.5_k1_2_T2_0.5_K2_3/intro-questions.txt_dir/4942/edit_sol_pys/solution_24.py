

def main():
    with open('in.txt', 'r') as f:
        n = int(f.readline())
        if n == 1:
            print(int(f.readline()))
        else:
            trees = [int(x) for x in f.readline().split()]
            trees.sort()
            max_days = 0
            for i in range(n):
                max_days = max(max_days, trees[i] + n - i)
            print(max_days)




if __name__ == '__main__':
    main()
