
import math

def main():
    A, B = map(int, input().split())
    print(A * B // math.gcd(A, B))
