

N, D = map(int, input().split())

print(N//(D*2+1)+(1 if N%(D*2+1) != 0 else 0))
