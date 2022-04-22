import re


s = input()  # 入力した文字列を変数sに代入
s = s.replace('eraser', ' ')  # sのeraserを空白文字に置換
s = s.replace('erase', ' ')  # sのeraseを空白文字に置換
s = s.replace('dreamer', ' ')  # sのdreamerを空白文字に置換
s = s.replace('dream', ' ')  # sのdreamを空白文字に置換
s = s.replace(' ','')  # sの空白文字を削除

if len(s) == 0:  # 変数sの文字数が0ならYESを出力
    print('YES')
else:
    print('NO')
