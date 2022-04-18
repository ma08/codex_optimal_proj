

def check_assumptions(conclusion_list, assumption_list, conclusion_index):
    for assumption in assumption_list:
        if assumption not in conclusion_list[:conclusion_index]:
            return False
    return True

def main():
    N = int(input())
    conclusion_list = []
    for i in range(N):
        conclusion_list.append(input())

    for i in range(N):
        line = conclusion_list[i]
        if "->" not in line:
            print(i+1)
            return
        conclusion = line.split("->")[1].strip()
        assumptions = line.split("->")[0].split(" ")
        if i == 0:
            print(i+1)
            return
        if check_assumptions(conclusion_list, assumptions, i):
            continue
        else:
            print(i+1)
            return

    print("correct")

if __name__ == "__main__":
    main()
