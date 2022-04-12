
def find_pink(colors):
    pink = ['pink', 'PINK', 'Pink', 'PinK', 'pinK', 'piNk', 'pInk', 'PInk', 'PINKrose', 'pinkrose', 'Pinkrose', 'PinKrose', 'pinKrose', 'piNkrose', 'pInkrose', 'PInkrose', 'PINKRose', 'pinkRose', 'PinkRose', 'PinKRose', 'pinKRose', 'piNkRose', 'pInkRose', 'PInkRose', 'PINKROSE', 'pinkROSE', 'PinkROSE', 'PinKROSE', 'pinKROSE', 'piNkROSE', 'pInkROSE', 'PInkROSE']
    if colors in pink:
        return True
    return False

def main():
    n = int(input())
    count = 0
    for i in range(n):
        colors = input()
        if find_pink(colors):
            count += 1
    if count == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(count)

if __name__ == "__main__":
    main()
