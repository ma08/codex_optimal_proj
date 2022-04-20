

def main():
    """
    入力された数字を取得
    """
    num_list = []
    num_list = input().split(" ")
    num_n = int(num_list[0])
    num_m = int(num_list[1])

    """
    データを取得
    """
    data_list = []
    for i in range(num_n):
        data_list.append(input().split(" "))

    """
    データを整理
    """
    for i in range(num_n):
        data_list[i][0] = int(data_list[i][0])
        for j in range(data_list[i][0]):
            data_list[i][j+1] = int(data_list[i][j+1])

    """
    全員が好きな食べ物の数を数える
    """
    count = 0
    for i in range(num_m):
        food_check = 0
        for j in range(num_n):
            for k in range(data_list[j][0]):
                if i+1 == data_list[j][k+1]:
                    food_check += 1
                    break
        if food_check == num_n:
            count += 1

    print(count)

if __name__ == "__main__":
    main()