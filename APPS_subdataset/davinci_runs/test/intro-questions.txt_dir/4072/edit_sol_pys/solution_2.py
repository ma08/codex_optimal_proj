
def solution(year):
    return 1 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 0

if __name__ == "__main__":
    print(solution(int(input())))
