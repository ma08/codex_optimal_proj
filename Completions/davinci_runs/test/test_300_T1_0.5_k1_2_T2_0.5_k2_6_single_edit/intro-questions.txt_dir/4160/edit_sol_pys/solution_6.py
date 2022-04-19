
with open('input.txt') as f:
    x = int(f.readline())
    year = 0
    balance = 100
    while balance < x:
        balance += balance // 100
        year += 1
    with open('output.txt', 'w') as o:
        o.write(str(year))
