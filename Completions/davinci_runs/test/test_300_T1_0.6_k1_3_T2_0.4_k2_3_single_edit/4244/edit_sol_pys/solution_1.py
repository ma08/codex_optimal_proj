

def main():
    _ = int(input())
    positions = [int(x) for x in input().split()]
    positions.sort()
    meeting_point = positions[len(positions) // 2]
    total_stamina = 0
    for pos in positions:
        total_stamina += (pos - meeting_point) ** 2
    print(total_stamina)

if __name__ == '__main__':
    main()
