

def main():
    """
    main function
    """
    n, r = map(int, input().split())
    arr = list(map(int, input().split()))
    heater = 0
    heater_arr = []
    for i in range(n):
        if arr[i] == 1:
            heater_arr.append(i+1)

    if heater_arr == []:
        print(-1)
    else:
        i = 0
        while i < len(heater_arr):
            if i == 0:
                if heater_arr[i] - 1 > r:
                    heater += 1
                    i += 1
                else:
                    heater += 1
                    i += 1
            else:
                if heater_arr[i] - heater_arr[i-1] > 2*r:
                    heater += 1
                    i += 1
                else:
                    i += 1
        print(heater)


main()