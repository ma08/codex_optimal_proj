

def main():
    N = int(input())
    conclusion_list = [input()]
    for i in range(N):
        line = input()
        if "->" in line:
            conclusion = line.split("->")[1].strip()
            assumptions = line.split("->")[0].split(" ")
            for assumption in assumptions:
                if assumption not in conclusion_list:
                    print(i + 1)
                    return
        else:
            print(i + 1)
            return
        conclusion_list.append(conclusion)

    print("correct")

if __name__ == "__main__":
    main()
