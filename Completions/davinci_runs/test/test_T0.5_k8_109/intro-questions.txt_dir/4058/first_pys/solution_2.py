

def main():
    # read input
    n, r = map(int, input().split())
    a = list(map(int, input().split()))

    # find heaters and unheated positions
    heaters = [i for i in range(n) if a[i]]
    unheated = [i for i in range(n) if not a[i]]

    # find the minimum number of heaters needed to warm up the whole house
    ans = 0
    for pos in unheated:
        # find the closest heater to the left
        left = 0
        right = len(heaters) - 1
        while left < right:
            mid = (left + right) // 2
            if heaters[mid] < pos:
                left = mid + 1
            else:
                right = mid
        if heaters[left] >= pos:
            left -= 1

        # find the closest heater to the right
        left = 0
        right = len(heaters) - 1
        while left < right:
            mid = (left + right) // 2
            if heaters[mid] <= pos:
                left = mid + 1
            else:
                right = mid

        # if the closest heaters cannot warm up the position, add a new heater
        if left >= len(heaters) or heaters[left] > pos + r - 1:
            ans += 1
            heaters.insert(left, pos)

    print(ans)


if __name__ == "__main__":
    main()