

num = int(input()) # リストの長さ
input_list = list(map(int, input().split())) # 入力されたリスト

for i in input_list:
    if i % 2 == 0:
        if i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            exit(0)
print("APPROVED")
