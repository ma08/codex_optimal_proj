def find_digit(n):
    return int(str(n)[-1])

if __name__ == '__main__':
    q = int(input())
    for _ in range(q): 
        n = int(input())
        print(find_digit(n))
