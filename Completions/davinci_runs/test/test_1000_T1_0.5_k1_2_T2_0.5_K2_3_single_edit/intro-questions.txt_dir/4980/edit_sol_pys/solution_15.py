

def find_pink(colors):
    pink = ['pink', 'PINK', 'Pink', 'PinK', 'pinK', 'piNk', 'pInk', 'PInk', 'PINKrose', 'pinkrose', 'Pinkrose', 'PinKrose', 'pinKrose', 'piNkrose', 'pInkrose', 'PInkrose', 'PINKRose', 'pinkRose', 'PinkRose', 'PinKRose', 'pinKRose', 'piNkRose', 'pInkRose', 'PInkRose', 'PINKROSE', 'pinkROSE', 'PinkROSE', 'PinKROSE', 'pinKROSE', 'piNkROSE', 'pInkROSE', 'PInkROSE']
    count = 0
    for color in colors:
        if color in pink:
            count += 1
    return count

def main():
    n = int(input())
    colors = []
    for i in range(n): # input all colors
        colors.append(input())
    count = find_pink(colors)
    if count == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(count)

if __name__ == "__main__":
    main()
