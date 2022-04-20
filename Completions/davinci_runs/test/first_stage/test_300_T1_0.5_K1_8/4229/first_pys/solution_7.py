

n = int(input())

div3 = n // 3
div5 = n // 5
div15 = n // 15

def sum_div(n, d):
    return d * (d + 1) * n // 2

print(sum_div(div3, 3) + sum_div(div5, 5) - sum_div(div15, 15))