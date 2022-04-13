

    # 文字列を受け取る。
if __name__ == '__main__':
    S = input()
    if len(S) == len(set(S)):
        print("yes")
    else:
        print("no")
