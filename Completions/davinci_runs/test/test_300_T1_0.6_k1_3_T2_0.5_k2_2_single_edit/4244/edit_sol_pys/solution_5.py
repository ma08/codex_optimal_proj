

    """
    input:
    3
    1 3 2
    output:
    2
    """
def main():
    num_people = int(input())
    positions = [int(x) for x in input().split()] # [1, 3, 2]
    positions.sort()
    mid = len(positions) // 2 # 1
    meeting_point = positions[mid]
    total_stamina = 0
    for pos in positions:
        total_stamina += (pos - meeting_point) ** 2
    print(total_stamina)

if __name__ == '__main__':
    main()
