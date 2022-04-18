from operator import itemgetter

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
max_a = a[0]
second_a = a[1]

b = list(map(int, input().split()))
b.sort(reverse=True)
max_b = b[0]
second_b = b[1]

c = list(map(int, input().split()))
c.sort(reverse=True)
max_c = c[0]
second_c = c[1]

max_a_b = max_a * max_b
second_a_b = max_a * second_b
max_a_c = max_a * max_c
second_a_c = max_a * second_c

max_b_c = max_b * max_c
second_b_c = max_b * second_c

second_a_b_c = second_a * max_b * max_c

max_abc = max(max_a_b, second_a_b, max_a_c, second_a_c, max_b_c, second_b_c, second_a_b_c)
print(max_abc)
