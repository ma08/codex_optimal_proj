import os
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())

    for i in [p, m, g]:  # 각 사람들의 입장 시간
        if i > a:  # 각 사람들의 입장 시간이 지하철이 떠나는 시간보다 클 경우
            if (i - a) % (b + a) < a:  # 지하철이 떠나는 시간보다 지하철 도착 시간이 클 경우
                print('both')  # 지하철이 도착하고 곧 떠나는 상황
            else:  # 지하철이 도착하고 곧 떠나는 상황이 아닐 경우
                print('one')  # 지하철이 떠나는 상황
        else:  # 각 사람들의 입장 시간이 지하철이 떠나는 시간보다 작을 경우
            print('both')  # 지하철이 도착하고 곧 떠나는 상황

        if i > c:  # 각 사람들의 입장 시간이 버스가 떠나는 시간보다 클 경우
            if (i - c) % (c + d) < c:  # 버스가 떠나는 시간보다 버스 도착 시간이 클 경우
                print('both')  # 버스가 도착하고 곧 떠나는 상황
            else:  # 버스가 도착하고 곧 떠나는 상황이 아닐 경우
                print('one')  # 버스가 떠나는 상황
        else:  # 각 사람들의 입장 시간이 버스가 떠나는 시간보다 작을 경우
            print('both')  # 버스가 도착하고 곧 떠나는 상황


if __name__ == '__main__':
    main()
