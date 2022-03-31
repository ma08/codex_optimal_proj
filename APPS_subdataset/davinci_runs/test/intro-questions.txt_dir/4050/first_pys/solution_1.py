

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    sums = []
    num_sets = []
    for i in range(n):
        for j in range(i+1, n+1):
            sums.append(sum(nums[i:j]))
            num_sets.append([i,j-1])
    sums.sort()
    max_count = 0
    for i in range(len(sums)-1, 0, -1):
        if sums[i] == sums[i-1]:
            max_count += 1
        else:
            break
    print(max_count+1)
    for i in range(len(sums)-1, len(sums)-max_count-2, -1):
        print(str(num_sets[i][0]+1) + " " + str(num_sets[i][1]+1))

main()