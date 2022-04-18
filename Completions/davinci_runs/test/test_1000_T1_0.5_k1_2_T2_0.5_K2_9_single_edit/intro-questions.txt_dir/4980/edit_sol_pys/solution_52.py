
def find_pink(color):
    pink = ['pink', 'PINK', 'Pink', 'PinK', 'pinK', 'piNk', 'pInk', 'PInk',
            'PINKrose', 'pinkrose', 'Pinkrose', 'PinKrose', 'pinKrose', 'piNkrose', 'pInkrose', 'PInkrose',
            'PINKRose', 'pinkRose', 'PinkRose', 'PinKRose', 'pinKRose', 'piNkRose', 'pInkRose', 'PInkRose',
            'PINKROSE', 'pinkROSE', 'PinkROSE', 'PinKROSE', 'pinKROSE', 'piNkROSE', 'pInkROSE', 'PInkROSE']
    if color in pink:
        return True
    return False


def main():
    n = int(input())
    count = 0
    for i in range(n):
        color = input()
        if find_pink(color):
            count += 1
    if count == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(count)


if __name__ == "__main__":
    main()
