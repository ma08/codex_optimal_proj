

a, b, x = map(int, input().split())  # a, b, x をスペース区切りで入力

ans = "0" * a + "1" * b  # a個の0とb個の1を結合してansに代入

for i in range(x):
    if ans[i] == "0":
        ans = ans[:i] + "1" + ans[i+1:]  # ansのi番目の文字を1に置き換える
    else:
        ans = ans[:i] + "0" + ans[i+1:]  # ansのi番目の文字を0に置き換える

print(ans)
