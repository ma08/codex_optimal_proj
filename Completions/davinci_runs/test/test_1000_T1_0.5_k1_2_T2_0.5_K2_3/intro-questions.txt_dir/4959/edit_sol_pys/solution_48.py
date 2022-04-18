def main():
    e, f, c = map(int, input().split())
    count = 0
    while e + f >= c:  # 가지고 있는 캔이 c보다 크거나 같을 때
        count += (e + f) // c  # 캔을 바꾸어서 가지고 있는 캔을 c로 나눈 몫만큼 더한다.
        e, f = (e + f) % c, e + f // c  # 가지고 있는 캔을 c로 나눈 나머지를 잔에 담고, c로 나눈 몫을 바구니에 담는다.
    print(count)


if __name__ == "__main__":
    main()
