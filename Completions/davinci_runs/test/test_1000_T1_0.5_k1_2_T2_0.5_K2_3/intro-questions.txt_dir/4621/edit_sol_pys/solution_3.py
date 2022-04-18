

def main():
    h, w = map(int, input().split())
    matrix = [input() for _ in range(h)]
    for _ in range(2):
        for i in range(h):
            print(matrix[i])

if __name__ == '__main__':
    main()
