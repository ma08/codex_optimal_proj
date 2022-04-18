

def main():
    a, b = map(int, input().split())
    m, sigma = map(float, input().split())

    if sigma > m:
        print(0)
    else:
        print(max(0, (m-sigma)*a + sigma*b//2))
