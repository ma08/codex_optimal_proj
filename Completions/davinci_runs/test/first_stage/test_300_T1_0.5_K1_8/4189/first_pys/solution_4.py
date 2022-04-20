

def main():
    n = int(input())
    cheeses = []
    for i in range(n):
        name, type = input().split(" ")
        cheeses.append([name, type])

    count = 0
    for i in range(len(cheeses)):
        for j in range(i+1, len(cheeses)):
            for k in range(j+1, len(cheeses)):
                if cheeses[i][1] != cheeses[j][1] and cheeses[j][1] != cheeses[k][1] and cheeses[k][1] != cheeses[i][1]:
                    count += 1

    print(count)

main()