

def main():
    N = int(input())
    conclusion_list = []
    for i in range(N):
        conclusion_list.append(input())

    for i in range(N):
        line = conclusion_list[i]
        if "->" in line:
            if i == 0:
                print(i + 1)
                return
            conclusion = line.split("->")[1].strip()
            assumptions = line.split("->")[0].split(" ")
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
