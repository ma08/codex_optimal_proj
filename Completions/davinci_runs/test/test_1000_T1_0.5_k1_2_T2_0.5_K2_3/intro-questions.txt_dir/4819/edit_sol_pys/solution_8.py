

def main():
    nums = []
    for _ in range(10):
        nums.append(int(input()))
    modulo_nums = [num % 42 for num in nums]
    print(len(set(modulo_nums)))

if __name__ == "__main__":
    main()
