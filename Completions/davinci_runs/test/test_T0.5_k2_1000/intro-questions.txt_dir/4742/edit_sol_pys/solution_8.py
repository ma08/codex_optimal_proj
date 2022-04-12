

def main():
    notes = "C C# D D# E F F# G G# A A# B".split()  # 创建音符列表
    n = int(input().strip())
    m1 = input().strip().split()  # 输入第一行音符
    m2 = input().strip().split()  # 输入第二行音符
    if m1 == m2:  # 如果两行音符完全相同
        print("Nonsense")
    elif m1 == m2[::-1]:  # 如果两行音符反向相同
        print("Retrograde")
    elif m2 == m1[::-1]:
        print("Retrograde")
    else:
        for i in range(len(m1)):
            if m2[i] == notes[(notes.index(m1[i]) + n) % 12]:  # 如果是转位
                print("Transposition")
                break
            if m2[i] == notes[(notes.index(m1[0]) - (notes.index(m1[i]) - notes.index(m1[0]))) % 12]:  # 如果是倒位
                print("Inversion")
                break
        else:
            print("Nonsense")

if __name__ == "__main__":
    main()
