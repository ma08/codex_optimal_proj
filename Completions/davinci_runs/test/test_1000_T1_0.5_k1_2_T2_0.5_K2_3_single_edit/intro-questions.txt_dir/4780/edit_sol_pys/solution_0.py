

def solution(n, m, line1, line2):
    count = 0
    # if len(line1) == 0 or len(line2) == 0:
    #     return count

    while len(line1) > 0 and len(line2) > 0:
        if line1[0] == line2[-1]:
            line1 = line1[1:]
            line2 = line2[:-1]
            count += 1
        else:
            if line1[0] > line2[-1]:
                line1 = line1[1:]
                line2 = line2[:-1]
            else:
                line1 = line1[1:]
                line2 = line2[:-2]
    return count

def main():
    N1, N2 = (int(x) for x in input().split())
    line1 = input()
    line2 = input()
    print(solution(N1, N2, line1, line2))

if __name__ == "__main__":
    main()
