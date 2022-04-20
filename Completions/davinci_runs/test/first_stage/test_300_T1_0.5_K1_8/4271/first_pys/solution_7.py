

n = int(input())
dishes = list(map(int, input().split()))
satisfactions = [0] + list(map(int, input().split()))
bonuses = [0] + list(map(int, input().split()))

print(sum([satisfactions[dishes[i]] + bonuses[dishes[i-1]] for i in range(1, n)]))