

if __name__ == '__main__':
    n = int(input())
    print("Weird") if n % 2 == 1 else print("Not Weird") if n >= 2 and n <= 5 else print("Weird") if n >= 6 and n <= 20 else print("Not Weird")
