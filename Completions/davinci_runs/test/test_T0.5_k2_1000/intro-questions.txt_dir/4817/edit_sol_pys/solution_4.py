

def next_permutation(a):  # 次の順列を生成する
    n = len(a)
    i = n - 1
    while i > 0 and a[i - 1] >= a[i]:  # 後ろから見ていって、逆順になっているところを探す
        i -= 1
    if i <= 0:
        return False
    j = n - 1
    while a[j] <= a[i - 1]:  # 後ろから見ていって、a[i-1]より大きい数字を探す
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]  # その数字とa[i-1]を入れ替える
    a[i:] = reversed(a[i:])  # それ以降を逆順にする

    return True

def main():
    s = input()
    a = [int(x) for x in s]
    if next_permutation(a):
        print(''.join([str(x) for x in a]))
    else:
        print(0)


if __name__ == "__main__":
    main()
