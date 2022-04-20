

def main(A, B):
    return A * B

if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = main(A, B)
    print(ans)
