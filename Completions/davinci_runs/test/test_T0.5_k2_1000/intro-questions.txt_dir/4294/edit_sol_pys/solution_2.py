

def main():
    # Read input
    x, a = [int(i) for i in input().split()]  # split()で区切られた文字列をリストに格納

    # Compare the two values and print the result
    if x < a:
        print(0)  # 出力はprint()で行う
    else:
        print(10)

if __name__ == '__main__':
    main()
