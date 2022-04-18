

# 入力された数値のうち大きい方を2回押す
def push_button(a, b):
    return a + b - max(a, b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(push_button(a, b))
