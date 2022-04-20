


def min_sum_of_flight_times(a, b, c):
    return min(a + b, a + c, b + c)


if __name__ == "__main__":
    p, q, r = map(int, input().split())
    print(min_sum_of_flight_times(p, q, r))