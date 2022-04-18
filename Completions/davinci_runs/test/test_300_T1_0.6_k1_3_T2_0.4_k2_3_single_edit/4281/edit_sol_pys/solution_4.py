

def get_answer(x):
    pass


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    answer = get_answer(x)
    print("{} {}".format(answer[0], answer[1]))
