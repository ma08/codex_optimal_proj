

import sys

def main():
    v2, v3, v5, v7, v11, v13, v17, v19 = map(int, input().split())
    N = 0
    while True:
        if v2 == 1 and v3 == 2 and v5 == 4 and v7 == 6 and v11 == 10 and v13 == 12 and v17 == 16 and v19 == 18:
            break
        else:
            v2 = (v2 + 1) % 2
            if v2 == 1:
                v3 = (v3 + 1) % 3
                if v3 == 2:
                    v5 = (v5 + 1) % 5
                    if v5 == 4:
                        v7 = (v7 + 1) % 7
                        if v7 == 6:
                            v11 = (v11 + 1) % 11
                            if v11 == 10:
                                v13 = (v13 + 1) % 13
                                if v13 == 12:
                                    v17 = (v17 + 1) % 17
                                    if v17 == 16:
                                        v19 = (v19 + 1) % 19
                                        if v19 == 18:
                                            sys.exit(0)
        N += 1
    print(N)

main()
