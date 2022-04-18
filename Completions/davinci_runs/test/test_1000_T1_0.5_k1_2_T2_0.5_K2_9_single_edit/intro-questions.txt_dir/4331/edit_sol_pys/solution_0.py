
N = int(input()) #int型で入力を受け取る
if N % 10 == 7: #10で割った余りが7の場合
    print('Yes') #Yesと表示する
elif N // 10 % 10 == 7: #10で割った商を10で割った余りが7の場合
    print('Yes') #Yesと表示する
elif N // 100 == 7: #100で割った商が7の場合
    print('Yes') #Yesと表示する
else: #それ以外の場合
    print('No') #Noと表示する
