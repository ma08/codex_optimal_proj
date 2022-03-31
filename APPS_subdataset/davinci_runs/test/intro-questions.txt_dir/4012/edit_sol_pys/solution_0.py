

import math

def gcd(a, b):
    return (a*b)//math.gcd(a, b)

def lcm(a, b):
    return (a*b)//math.gcd(a, b)

def main():
    t = int(input())
    for i in range(t):
        a, b, c = [int(x) for x in input().split()]
        A, B, C = a, b, c
        gcd_ab = gcd(a, b)
        gcd_ac = gcd(a, c)
        gcd_bc = gcd(b, c)
        large_gcd = max(gcd_ab, gcd_ac, gcd_bc)
        A, B, C = a, b, c
        if large_gcd == gcd_ab:
            lcm_bc = lcm(b, c)
            lcm_ac = lcm(a, c)
            small_lcm = min(lcm_bc, lcm_ac)
            if small_lcm == lcm_bc:
                A, B = b, lcm_bc
            else:
                B, C = lcm_ac, c
        elif large_gcd == gcd_ac:
            lcm_bc = lcm(b, c)
            lcm_ab = lcm(a, b)
            small_lcm = min(lcm_bc, lcm_ab)
            if small_lcm == lcm_bc:
                A, B = b, lcm_bc
            else:
                A, B = lcm_ab, b
        else:
            lcm_ac = lcm(a, c)
            lcm_ab = lcm(a, b)
            small_lcm = min(lcm_ac, lcm_ab)
            if small_lcm == lcm_ac:
                B, C = lcm_ac, c
            else:
                A, B = lcm_ab, b
        res = sum(x-y for x, y in zip([A, B, C], [a, b, c]))
        print(res)
        print(A, B, C)

if __name__ == "__main__":
    main()
