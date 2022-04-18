import math

def main():
    R, C = map(int, input().split())
    pizza_area = math.pi * (R ** 2) # 전체 피자 면적
    cheese_area = pizza_area - math.pi * ((R - C) ** 2) # 치즈 면적
    print(100 * (cheese_area / pizza_area)) # 치즈 면적을 피자 면적으로 나눈 값을 백분율로 출력


if __name__ == "__main__":
    main()
