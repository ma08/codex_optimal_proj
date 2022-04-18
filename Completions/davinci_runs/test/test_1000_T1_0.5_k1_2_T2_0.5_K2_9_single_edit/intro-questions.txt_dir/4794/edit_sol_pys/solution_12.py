import math


r, c = map(int, input().split())  # 入力された数をr,cに代入
parking = [input() for _ in range(r)]  # 入力された数をparkingに代入

squash = [0, 0, 0, 0, 0]  # squashを0で初期化
for i in range(r-1):  # r-1回ループ
    for j in range(c-1):  # c-1回ループ
        if parking[i][j] == "#":  # parking[i][j]が#なら
            continue
        elif parking[i][j] == ".":  # parking[i][j]が.なら
            if parking[i+1][j] == "X" and parking[i][j+1] == "X" and parking[i+1][j+1] == "X":  # 下と右と右下がXなら
                squash[4] += 1  # squash[4]を+1
            elif parking[i+1][j] == "X" and parking[i][j+1] == "X":  # 下と右がXなら
                squash[3] += 1  # squash[3]を+1
            elif parking[i+1][j] == "X" and parking[i+1][j+1] == "X":  # 下と右下がXなら
                squash[3] += 1  # squash[3]を+1
            elif parking[i][j+1] == "X" and parking[i+1][j+1] == "X":  # 右と右下がXなら
                squash[3] += 1  # squash[3]を+1
            elif parking[i+1][j] == "X":  # 下がXなら
                squash[2] += 1  # squash[2]を+1
            elif parking[i][j+1] == "X":  # 右がXなら
                squash[2] += 1  # squash[2]を+1
            elif parking[i+1][j+1] == "X":  # 右下がXなら
                squash[2] += 1  # squash[2]を+1
            else:
                squash[0] += 1  # それ以外ならsquash[0]を+1
        else:  # parking[i][j]がXなら
            squash[1] += 1  # squash[1]を+1

print(squash[0])  # squash[0]を出力
print(squash[1])  # squash[1]を出力
print(squash[2])  # squash[2]を出力
print(squash[3])  # squash[3]を出力
print(squash[4])  # squash[4]を出力
