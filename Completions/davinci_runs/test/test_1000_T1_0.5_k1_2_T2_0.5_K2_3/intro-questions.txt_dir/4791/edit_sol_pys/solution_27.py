
import sys

def main():
    s = [int(x) for x in sys.stdin.readline().split()] # edges of quadrilateral
    max_area = 0
    for i in range(4):
        for j in range(i+1,4):
            for k in range(j+1,4):
                for l in range(k+1,4):
                    area = area_of_quadrilateral(s[i], s[j], s[k], s[l]) # area of quadrilateral
                    if area > max_area:
                        max_area = area
    print(max_area)

def area_of_quadrilateral(a, b, c, d):
    s = (a + b + c + d) / 2 # semiperimeter
    return (s - a) * (s - b) * (s - c) * (s - d) ** 0.5 # Heron's formula, square root

if __name__ == '__main__':
    main()
