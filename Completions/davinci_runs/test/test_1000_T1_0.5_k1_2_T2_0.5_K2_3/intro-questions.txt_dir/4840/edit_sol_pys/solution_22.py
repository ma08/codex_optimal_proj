
a1, b1, a2, b2 = map(int, input().split())
c1, d1, c2, d2 = map(int, input().split())

p1 = (b1-a1+1) * (b2-a2+1)
p2 = (d1-c1+1) * (d2-c2+1)

print("Tie" if p1 == p2 else "Emma" if p1 > p2 else "Gunnar")
