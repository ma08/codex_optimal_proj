

def main():
    K = int(input())
    desks = [int(input()) for i in range(K)]
    current_pass = 1
    passes = 0
    while any(d > current_pass for d in desks):
        current_pass = max(d for d in desks if d <= current_pass)
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
