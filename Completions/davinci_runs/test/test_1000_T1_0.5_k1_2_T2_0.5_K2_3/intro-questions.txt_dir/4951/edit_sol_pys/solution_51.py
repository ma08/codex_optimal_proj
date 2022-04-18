

def main():
    N = int(input())
    conclusion_list = list()
    for i in range(N):
        conclusion_list.append(input().strip())

    for i in range(N):
        line = conclusion_list[i]
        if "->" in line and "|" not in line:
            conclusion = line.split("->")[1].strip()[1:-1]
            assumptions = line.split("->")[0].split("&")[:-1]
            for assumption in assumptions:
                if assumption not in conclusion_list[:i]:
                    print(i + 1)
                    return
        else:
            print(i + 1)
            return

    print("correct")


if __name__ == "__main__":
    main()
