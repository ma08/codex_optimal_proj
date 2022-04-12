

def main():
    N = int(input())
    conclusion_list = [None] * N
    for i in range(N):
        conclusion_list[i] = input()

    for i in range(N):
        line = conclusion_list[i]
        if "->" in line:
            if i == 0:
                print(i + 1)
                return
            conclusion = line.split("->")[1].strip()  # вывод
            assumptions = line.split("->")[0].split(" ")  # предположения
            for assumption in assumptions:
                if assumption not in conclusion_list[:i]:  # если предположения нет в списке
                    print(i + 1)
                    return
        else:  # если вывод не имеет предположений
            print(i + 1)
            return

    print("correct")

if __name__ == "__main__":
    main()
