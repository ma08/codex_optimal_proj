

def main():
    num_people = int(input())
    positions = [int(x) for x in input().split()]
    positions.sort()
    mid = len(positions) // 2
    meeting_point = positions[mid]
    total_stamina = 0
    for pos in positions:
        total_stamina += abs(pos - meeting_point)
    print(total_stamina)

if __name__ == '__main__':
    main()
