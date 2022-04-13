


def print_staff(staff):
    for key in ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']:
        print(key+': '+staff[key])


def main():
    n = int(input())
    notes = input().split()
    staff = {'G':'', 'F':'', 'E':'', 'D':'', 'C':'', 'B':'', 'A':'',
             'g':'', 'f':'', 'e':'', 'd':'', 'c':'', 'b':'', 'a':''}
    for i in notes:
        staff[i[0]] += '*'*(len(i) if len(i) > 1 else 1)
    for key in ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']:
        print(key+': '+staff[key])

main()
