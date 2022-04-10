

def main():
    n = int(raw_input())
    a = raw_input()
    f = map(int, raw_input().split())

    f_map = {}
    for i in range(1, 10):
        f_map[str(i)] = str(f[i - 1])

    max_num = 0
    for i in range(n):
        for j in range(i, n):
            k = j
            while k < n:
                if int(a[j:k + 1]) > max_num:
                    max_num = int(a[j:k + 1])
                k += 1
            if int(a[j:k + 1]) > max_num:
                max_num = int(a[j:k + 1])
            s = a[i:j + 1]
            for key in f_map.keys():
                s = s.replace(key, f_map[key])
            if int(s) > max_num:
                max_num = int(s)
    print max_num

if __name__ == '__main__':
    main()