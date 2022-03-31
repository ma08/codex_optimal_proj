
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if k in d:
        print(0)
        return
    if k == 1:
        print(a[-1] - a[0])
        return
    if k == n:
        print(a[-1] - a[0])
        return
    if k == 2:
        if a[0] == a[1]:
            print(a[-1] - a[0])
            return
        else:
            print(max(a[-1] - a[1], a[-2] - a[0]))
            return
    if k == n - 1:
        if a[0] == a[1]:
            print(a[-2] - a[0])
            return
        else:
            print(max(a[-2] - a[1], a[-1] - a[0]))
            return
    if k == n - 2:
        if a[0] == a[1]:
            print(a[-3] - a[0])
            return
        else:
            print(max(a[-3] - a[1], a[-1] - a[0]))
            return
    if k == n - 3:
        if a[0] == a[1]:
            print(a[-4] - a[0])
            return
        else:
            print(max(a[-4] - a[1], a[-1] - a[0]))
            return
    if k == n - 4:
        if a[0] == a[1]:
            print(a[-5] - a[0])
            return
        else:
            print(max(a[-5] - a[1], a[-1] - a[0]))
            return
    if k == n - 5:
        if a[0] == a[1]:
            print(a[-6] - a[0])
            return
        else:
            print(max(a[-6] - a[1], a[-1] - a[0]))
            return
    if k == n - 6:
        if a[0] == a[1]:
            print(a[-7] - a[0])
            return
        else:
            print(max(a[-7] - a[1], a[-1] - a[0]))
            return
    if k == n - 7:
        if a[0] == a[1]:
            print(a[-8] - a[0])
            return
        else:
            print(max(a[-8] - a[1], a[-1] - a[0]))
            return
    if k == n - 8:
        if a[0] == a[1]:
            print(a[-9] - a[0])
            return
        else:
            print(max(a[-9] - a[1], a[-1] - a[0]))
            return
    if k == n - 9:
        if a[0] == a[1]:
            print(a[-10] - a[0])
            return
        else:
            print(max(a[-10] - a[1], a[-1] - a[0]))
            return
    if k == n - 10:
        if a[0] == a[1]:
            print(a[-11] - a[0])
            return
        else:
            print(max(a[-11] - a[1], a[-1] - a[0]))
            return
    if k == n - 11:
        if a[0] == a[1]:
            print(a[-12] - a[0])
            return
        else:
            print(max(a[-12] - a[1], a[-1] - a[0]))
            return
    if k == n - 12:
        if a[0] == a[1]:
            print(a[-13] - a[0])
            return
        else:
            print(max(a[-13] - a[1], a[-1] - a[0]))
            return
    if k == n - 13:
        if a[0] == a[1]:
            print(a[-14] - a[0])
            return
        else:
            print(max(a[-14] - a[1], a[-1] - a[0]))
            return
    if k == n - 14:
        if a[0] == a[1]:
            print(a[-15] - a[0])
            return
        else:
            print(max(a[-15] - a[1], a[-1] - a[0]))
            return
    if k == n - 15:
        if a[0] == a[1]:
            print(a[-16] - a[0])
            return
        else:
            print(max(a[-16] - a[1], a[-1] - a[0]))
            return
    if k == n - 16:
        if a[0] == a[1]:
            print(a[-17] - a[0])
            return
        else:
            print(max(a[-17] - a[1], a[-1] - a[0]))
            return
    if k == n - 17:
        if a[0] == a[1]:
            print(a[-18] - a[0])
            return
        else:
            print(max(a[-18] - a[1], a[-1] - a[0]))
            return
    if k == n - 18:
        if a[0] == a[1]:
            print(a[-19] - a[0])
            return
        else:
            print(max(a[-19] - a[1], a[-1] - a[0]))
            return
    if k == n - 19:
        if a[0] == a[1]:
            print(a[-20] - a[0])
            return
        else:
            print(max(a[-20] - a[1], a[-1] - a[0]))
            return
    if k == n - 20:
        if a[0] == a[1]:
            print(a[-21] - a[0])
            return
        else:
            print(max(a[-21] - a[1], a[-1] - a[0]))
            return
    if k == n - 21:
        if a[0] == a[1]:
            print(a[-22] - a[0])
            return
        else:
            print(max(a[-22] - a[1], a[-1] - a[0]))
            return
    if k == n - 22:
        if a[0] == a[1]:
            print(a[-23] - a[0])
            return
        else:
            print(max(a[-23] - a[1], a[-1] - a[0]))
            return
    if k == n - 23:
        if a[0] == a[1]:
            print(a[-24] - a[0])
            return
        else:
            print(max(a[-24] - a[1], a[-1] - a[0]))
            return
    if k == n - 24:
        if a[0] == a[1]:
            print(a[-25] - a[0])
            return
        else:
            print(max(a[-25] - a[1], a[-1] - a[0]))
            return
    if k == n - 25:
        if a[0] == a[1]:
            print(a[-26] - a[0])
            return
        else:
            print(max(a[-26] - a[1], a[-1] - a[0]))
            return
    if k == n - 26:
        if a[0] == a[1]:
            print(a[-27] - a[0])
            return
        else:
            print(max(a[-27] - a[1], a[-1] - a[0]))
            return
    if k == n - 27:
        if a[0] == a[1]:
            print(a[-28] - a[0])
            return
        else:
            print(max(a[-28] - a[1], a[-1] - a[0]))
            return
    if k == n - 28:
        if a[0] == a[1]:
            print(a[-29] - a[0])
            return
        else:
            print(max(a[-29] - a[1], a[-1] - a[0]))
            return
    if k == n - 29:
        if a[0] == a[1]:
            print(a[-30] - a[0])
            return
        else:
            print(max(a[-30] - a[1], a[-1] - a[0]))
            return
    if k == n - 30:
        if a[0] == a[1]:
            print(a[-31] - a[0])
            return
        else:
            print(max(a[-31] - a[1], a[-1] - a[0]))
            return
    if k == n - 31:
        if a[0] == a[1]:
            print(a[-32] - a[0])
            return
        else:
            print(max(a[-32] - a[1], a[-1] - a[0]))
            return
    if k == n - 32:
        if a[0] == a[1]:
            print(a[-33] - a[0])
            return
        else:
            print(max(a[-33] - a[1], a[-1] - a[0]))
            return
    if k == n - 33:
        if a[0] == a[1]:
            print(a[-34] - a[0])
            return
        else:
            print(max(a[-34] - a[1], a[-1] - a[0]))
            return
    if k == n - 34:
        if a[0] == a[1]:
            print(a[-35] - a[0])
            return
        else:
            print(max(a[-35] - a[1], a[-1] - a[0]))
            return
    if k == n - 35:
        if a[0] == a[1]:
            print(a[-36] - a[0])
            return
        else:
            print(max(a[-36] - a[1], a[-1] - a[0]))
            return
    if k == n - 36:
        if a[0] == a[1]:
            print(a[-37] - a[0])
            return
        else:
            print(max(a[-37] - a[1], a[-1] - a[0]))
            return
    if k == n - 37:
        if a[0] == a[1]:
            print(a[-38] - a[0])
            return
        else:
            print(max(a[-38] - a[1], a[-1] - a[0]))
            return
    if k == n - 38:
        if a[0] == a[1]:
            print(a[-39] - a[0])
            return
        else:
            print(max(a[-39] - a[1], a[-1] - a[0]))
            return
    if k == n - 39:
        if a[0] == a[1]:
            print(a[-40] - a[0])
            return
        else:
            print(max(a[-40] - a[1], a[-1] - a[0]))
            return
    if k == n - 40:
        if a[0] == a[1]:
            print(a[-41] - a[0])
            return
        else:
            print(max(a[-41] - a[1], a[-1] - a[0]))
            return
    if k == n - 41:
        if a[0] == a[1]:
            print(a[-42] - a[0])
            return
        else:
            print(max(a[-42] - a[1], a[-1] - a[0]))
            return
    if k == n - 42:
        if a[0] == a[1]:
            print(a[-43] - a[0])
            return
        else:
            print(max(a[-43] - a[1], a[-1] - a[0]))
            return
    if k == n - 43:
        if a[0] == a[1]:
            print(a[-44] - a[0])
            return
        else:
            print(max(a[-44] - a[1], a[-1] - a[0]))
            return
    if k == n - 44:
        if a[0] == a[1]:
            print(a[-45] - a[0])
            return
        else:
            print(max(a[-45] - a[1], a[-1] - a[0]))
            return
    if k == n - 45:
        if a[0] == a[1]:
            print(a[-46] - a[0])
            return
        else:
            print(max(a[-46] - a[1], a[-1] - a[0]))
            return
    if k == n - 46:
        if a[0] == a[1]:
            print(a[-47] - a[0])
            return
        else:
            print(max(a[-47] - a[1], a[-1] - a[0]))
            return
    if k == n - 47:
        if a[0] == a[1]:
            print(a[-48] - a[0])
            return
        else:
            print(max(a[-48] - a[1], a[-1] - a[0]))
            return
    if k == n - 48:
        if a[0] == a[1]:
            print(a[-49] - a[0])
            return
        else:
            print(max(a[-49] - a[1], a[-1] - a[0]))
            return
    if k == n - 49:
        if a[0] == a[1]:
            print(a[-50] - a[0])
            return
        else:
            print(max(a[-50] - a[1], a[-1] - a[0]))
            return
    if k == n - 50:
        if a[0] == a[1]:
            print(a[-51] - a[0])
            return
        else:
            print(max(a[-51] - a[1], a[-1] - a[0]))
            return
    else:
        print(0)
        return

if __name__ == "__main__":
    main()