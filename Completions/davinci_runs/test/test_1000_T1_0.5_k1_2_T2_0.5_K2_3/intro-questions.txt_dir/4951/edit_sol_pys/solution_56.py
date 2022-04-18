

def main():
    N = int(input())
    conclusion_list = []  # список высказываний
    for i in range(N):  # перебираем высказывания
        conclusion_list.append(input())

    for i in range(N):
        line = conclusion_list[i]
        if "->" in line:  # если в высказывании есть импликация
            if i == 0:  # если высказывание первое
                print(i+1)
                return
            conclusion = line.split("->")[1].strip()  # заносим высказывание в переменную
            assumptions = line.split("->")[0].split(" ")  # список предпосылок
            for assumption in assumptions:  # перебираем предпосылки
                if assumption not in conclusion_list[:i]:  # если предпосылка не содержится в предыдущих высказываниях
                    print(i+1)
                    return
        else:  # если в высказывании нет импликации
            print(i+1)
            return


    print("correct")

if __name__ == "__main__":
    main()
