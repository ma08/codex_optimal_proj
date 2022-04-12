

def find_pink(color, pink):
    for i in range(len(pink)):
        if color == pink[i]:
            return True
    return False 

def main():
    n = int(input())
    pink = ['pink', 'PINK', 'Pink', 'PinK', 'pinK', 'piNk', 'pInk', 'PInk', 'PINKrose', 'pinkrose', 'Pinkrose', 'PinKrose', 'pinKrose', 'piNkrose', 'pInkrose', 'PInkrose', 'PINKRose', 'pinkRose', 'PinkRose', 'PinKRose', 'pinKRose', 'piNkRose', 'pInkRose', 'PInkRose', 'PINKROSE', 'pinkROSE', 'PinkROSE', 'PinKROSE', 'pinKROSE', 'piNkROSE', 'pInkROSE', 'PInkROSE', 'PINKrose', 'pinkrose', 'Pinkrose', 'PinKrose', 'pinKrose', 'piNkrose', 'pInkrose', 'PInkrose', 'PINKRose', 'pinkRose', 'PinkRose', 'PinKRose', 'pinKRose', 'piNkRose', 'pInkRose', 'PInkRose', 'PINKROSE', 'pinkROSE', 'PinkROSE', 'PinKROSE', 'pinKROSE', 'piNkROSE', 'pInkROSE', 'PInkROSE']
    count = 0
    for i in range(n):
        color = input()
        if find_pink(color, pink):
            count += 1
    if count == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(count)

if __name__ == "__main__":
    main()
