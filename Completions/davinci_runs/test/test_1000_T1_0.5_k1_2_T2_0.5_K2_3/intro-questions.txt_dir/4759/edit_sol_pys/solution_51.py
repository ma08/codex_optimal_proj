

#n = int(input())
#at_bat = list(map(int, input().split()))
n = 3
at_bat = [3, 0, 2]

total_bases = 0
total_at_bat = 0

for at_bat in at_bat:
    if at_bat != -1:
        total_bases += at_bat
        total_at_bat += 1

print(total_bases / total_at_bat)
