

from decimal import Decimal
from sys import stdin

T, X = map(int, stdin.readline().split())

print(Decimal(T)/Decimal(X))