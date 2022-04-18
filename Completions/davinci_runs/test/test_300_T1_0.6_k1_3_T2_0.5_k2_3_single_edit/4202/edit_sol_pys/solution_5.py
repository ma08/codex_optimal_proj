

def main(L, R, K):
    ans = 2019
    for i in range(L, R-K+2):
        for j in range(i+1, i+K):
            ans = min(ans, i*j % 2019, j*i % 2019)
            if ans == 0:
                return 0
    return ans

if __name__ == "__main__":
    L, R = map(int, input().split())
    K = R - L + 1
    ans = main(L, R, K)
    print(ans)
