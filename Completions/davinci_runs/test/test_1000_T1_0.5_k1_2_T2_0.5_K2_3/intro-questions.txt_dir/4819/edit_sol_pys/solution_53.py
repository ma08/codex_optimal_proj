
def distinct_modulo42(nums):
    modulo_nums = [num % 42 for num in nums]  # 입력 받은 수들을 나눈 나머지를 리스트로 만듬
    return len(set(modulo_nums))

def main():
    nums = []
    for _ in range(10):
        nums.append(int(input()))
    print(distinct_modulo42(nums))

if __name__ == "__main__":
    main()
