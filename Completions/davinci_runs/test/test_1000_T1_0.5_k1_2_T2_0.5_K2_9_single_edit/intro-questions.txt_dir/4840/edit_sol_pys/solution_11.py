
def func(a, b, c, d):
    return (b - a + 1) * (d - c + 1)
a1, b1, a2, b2 = map(int, input().split())
c1, d1, c2, d2 = map(int, input().split())
p1 = func(a1, b1, a2, b2)
p2 = func(c1, d1, c2, d2)
print("Tie" if p1 == p2 else "Emma" if p1 < p2 else "Gunnar")
