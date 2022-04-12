
if __name__ == '__main__':
    s = input()
    if len(s) == len(set(s)): # set()は重複を削除する
        print("yes")
    else:
        print("no")
