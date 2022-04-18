from typing import List


def main():
    n = int(input())
    s_list: List[str] = []
    for i in range(n):
        s_list.append(input())
    s_list.sort()
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(10):
                if s_list[i][k] != s_list[j][k]:
                    break
                if k == 9:
                    count += 1
    print(count)


if __name__ == "__main__":
    main()
