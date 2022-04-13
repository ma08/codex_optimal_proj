

n = int(input())  # 输入一个数字

if n == 0:  # 如果是0，直接输出0
    print(0)
    exit()

ans = ""  # ans为最终的结果
while n != 0:  # 如果n不等于0
    if n % (-2) == 0:  # 如果n除以-2的余数是0
        ans += "0"  # ans加上0
        n = n // (-2)  # n等于n除以-2
    else:
        ans += "1"  # ans加上1
        n = n // (-2) + 1  # n等于n除以-2+1

print(ans[::-1])  # 输出ans的倒序
