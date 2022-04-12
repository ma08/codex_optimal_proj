#!/usr/bin/env python3

import math

def main():
    r, c = map(int, input().split()) # r: 円の半径, c: 円の中心からの距離
    area = math.pi * (r**2) # 円の面積
    cheese_area = area - math.pi * ((r-c)**2) # 円の中心からの距離がc以下の部分の面積
    print(cheese_area / area * 100) # 円の中心からの距離がc以下の部分の割合

if __name__ == "__main__":
    main()
