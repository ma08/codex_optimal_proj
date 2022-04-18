import sys

def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        sums = {}
        ret = 1
        for i in range(n):
            for j in range(i, n):
                s = sum(arr[i:j + 1])
                sums[s] = sums.get(s, 0) + 1
                ret = max(ret, sums[s])
        with open("output.txt", "w") as o:
            o.write(str(ret) + "\n")
            for i in range(n):
                for j in range(i, n):
                    s = sum(arr[i:j + 1])
                    if sums[s] == ret:
                        ret -= 1
                        o.write(str(i + 1) + " " + str(j + 1) + "\n")
                        break

if __name__ == '__main__':
    main()
