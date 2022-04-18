

#n = int(input())
#at_bat = list(map(int, input().split()))
n = 3
at_bat = [3, 0, 2]

total_bases = 0
total_at_bat = 0

for at_bat in at_bat:
    if at_bat != 0: # If at_bat is not -1, add at_bat to total_bases and add 1 to total_at_bat
        total_bases += at_bat # Add at_bat to total_bases
        total_at_bat += 1 # Add 1 to total_at_bat

print(total_bases / total_at_bat)
