

def main():
    n = int(input())
    count = 0
    for i in range(n):
        color = input()
        if color == 'pink' or color == 'PINK' or color == 'Pink' or color == 'PinK' or color == 'pinK' or color == 'piNk' or color == 'pInk' or color == 'PInk' or color == 'PINKrose' or color == 'pinkrose' or color == 'Pinkrose' or color == 'PinKrose' or color == 'pinKrose' or color == 'piNkrose' or color == 'pInkrose' or color == 'PInkrose' or color == 'PINKRose' or color == 'pinkRose' or color == 'PinkRose' or color == 'PinKRose' or color == 'pinKRose' or color == 'piNkRose' or color == 'pInkRose' or color == 'PInkRose' or color == 'PINKROSE' or color == 'pinkROSE' or color == 'PinkROSE' or color == 'PinKROSE' or color == 'pinKROSE' or color == 'piNkROSE' or color == 'pInkROSE' or color == 'PInkROSE':
            count += 1
    if count == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(count)

if __name__ == "__main__":
    main()
