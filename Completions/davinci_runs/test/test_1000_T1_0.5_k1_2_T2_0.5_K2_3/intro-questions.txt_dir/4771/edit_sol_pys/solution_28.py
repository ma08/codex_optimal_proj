
def main():
    n, V = map(int, input().split())
    box_volume = []
    for n in range(n):
        box_volume.append(int(input().split()[0]) * int(input().split()[1]) * int(input().split()[2]))
    print(max(box_volume) - V)


if __name__ == "__main__":
    main()
