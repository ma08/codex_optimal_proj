
import sys
a, b = map(int, input().split())

sys.stdout.write(str(min(a+b+a+b, a+b+b+a)))
