

"""
1. Find the largest common divisor of the three numbers
2. Find the smallest common multiple of the three numbers
3. Find the smallest common multiple of the two numbers that are not the largest common divisor
4. Find the smallest common multiple of the two numbers that are not the smallest common multiple
"""

import math

def lcd(a, b):
    return (a*b)//math.gcd(a, b)

def scm(a, b):
    return (a*b)//math.gcd(a, b)

def main():
    t = int(input())
    for i in range(t):
        a, b, c = [int(x) for x in input().split()]
        A, B, C = a, b, c
        lcd_ab = lcd(a, b)
        lcd_ac = lcd(a, c)
        lcd_bc = lcd(b, c)
        large_lcd = max(lcd_ab, lcd_ac, lcd_bc)
        A, B, C = a, b, c
        if large_lcd == lcd_ab:
            scm_bc = scm(b, c)
            scm_ac = scm(a, c)
            small_scm = min(scm_bc, scm_ac)
            if small_scm == scm_bc:
                A, B = b, scm_bc
            else:
                B, C = scm_ac, c
        elif large_lcd == lcd_ac:
            scm_bc = scm(b, c)
            scm_ab = scm(a, b)
            small_scm = min(scm_bc, scm_ab)
            if small_scm == scm_bc:
                A, B = b, scm_bc
            else:
                A, B = scm_ab, b
        else:
            scm_ac = scm(a, c)
            scm_ab = scm(a, b)
            small_scm = min(scm_ac, scm_ab)
            if small_scm == scm_ac:
                B, C = scm_ac, c
            else:
                A, B = scm_ab, b
        res = sum(x-y for x, y in zip([A, B, C], [a, b, c]))
        print(res)
        print(A, B, C)

if __name__ == "__main__":
    main()