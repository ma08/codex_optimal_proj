
def main():
    N, K = map(int, input().split())
    print((N-1) * (N-2) * (N-3) * (N-4) * (N-5) * (N-6) * (N-7) * (N-8) * (N-9) * (N-10) / (K-1) / (K-2) / (K-3) / (K-4) / (K-5) / (K-6) / (K-7) / (K-8) / (K-9) / (K-10))
if __name__ == '__main__':
    main()
