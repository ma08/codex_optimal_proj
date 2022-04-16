
def check_num(n):
    return n % sum([int(i) for i in str(n)]) == 0


n = int(input())

while True:
    n += 1
    if check_num(n):
        print(n)
        break
