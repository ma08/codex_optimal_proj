
import math


def get_swath(swather, time):
    return math.ceil(time / swather[0])


def get_time(swather, swath):
    return swath * swather[0]


def get_cost(swather, swath):
    return swather[1] * swath


def get_swath_cost(swather, swath):
    return get_cost(swather, swath) * swather[2]


def get_swath_time(swather, swath):
    return get_time(swather, swath) * swather[3]


def get_total_swath_time(swather, swath):
    return get_time(swather, swath) + get_swath_time(swather, swath)


def get_total_cost(swather, swath):
    return get_cost(swather, swath) + get_swath_cost(swather, swath)


def get_total_time(swather, swath):
    return get_time(swather, swath) + get_swath_time(swather, swath)


def get_total_time_cost(swather, swath):
    return get_total_cost(swather, swath) + get_total_time(swather, swath)


def main():
    swathers, swath_count = [int(x) for x in input().split()]
    swathers_times_costs = []
    for i in range(swathers): swathers_times_costs.append([int(x) for x in input().split()])
    swathers_times_costs = sorted(swathers_times_costs)
    for i in range(1, len(swathers_times_costs)):
        for j in range(swath_count):
            swathers_times_costs[i][j] += swathers_times_costs[i - 1][j]
    for i in range(swathers): print(swathers_times_costs[i][swath_count - 1], end=' ')


main()
