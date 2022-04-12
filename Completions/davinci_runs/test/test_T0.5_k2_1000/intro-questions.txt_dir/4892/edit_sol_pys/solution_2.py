

from sys import stdin

def main():
    n = int(stdin.readline().strip())
    password = [stdin.readline().strip().split(' ') for _ in range(n)]  # 读取数据
    password.sort(key=lambda x: x[1], reverse=True)  # 按照第二个元素排序
    sum = 0
    for i in range(n):
        sum += (i+1)*float(password[i][1])  # 加权求和
    print(sum)

if __name__ == '__main__':
    main()
