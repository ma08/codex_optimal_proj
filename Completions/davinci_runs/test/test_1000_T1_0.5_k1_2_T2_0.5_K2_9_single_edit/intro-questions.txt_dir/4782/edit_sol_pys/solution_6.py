
import fileinput

n, m = map(int, fileinput.input()[0].split())

print(m + (n - 1) * (n - m - 1))
