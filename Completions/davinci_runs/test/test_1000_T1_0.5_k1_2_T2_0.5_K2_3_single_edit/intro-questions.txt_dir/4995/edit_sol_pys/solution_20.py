
def main(): 
    N = int(input())
    wait_time = 0
    for _ in range(N):
        M, S = map(int, input().split())
        wait_time += S/M
    print(wait_time/N)
main()
