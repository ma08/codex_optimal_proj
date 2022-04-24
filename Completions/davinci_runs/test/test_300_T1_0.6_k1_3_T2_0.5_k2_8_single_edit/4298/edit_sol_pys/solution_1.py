
def main(n, d):
    num_inspectors = 0
    start = 1
    while start <= n:
        num_inspectors += 1
        start += 2 * d + 1
    return num_inspectors


assert (main(6, 2) == 2)
assert (main(15, 4) == 4)
assert (main(20, 5) == 4)
assert (main(1, 1) == 1)
