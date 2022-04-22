

N = int(input())  # ユーザーから入力を受け取る
x = list(map(int, input().split()))  # ユーザーから入力を受け取る
for i in range(N):  # N回繰り返す
    if x[i] == 0:
        print("All Good")
        exit()
print("No Luck")
