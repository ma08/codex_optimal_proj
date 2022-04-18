
n, m = map(int, input().split())
k = list(map(int, input().split()))
sales = {}
for _ in range(m):
    d, t = map(int, input().split())
    sales[d] = t

days = 0
for i in range(n):
    if k[i] > 0:
        on_sale = set()
        for d, t in sales.items():
            if t == i+1:
                on_sale.add(d)
        if len(on_sale) == 0:
            days += 2 * k[i]
        else:
            days += 1
            k[i] -= 1
            for d in on_sale:
                if k[i] > 0:
                    days += 1
                    k[i] -= 1
                else:
                    break
            if k[i] > 0:
                days += 2 * k[i]
print(days)
