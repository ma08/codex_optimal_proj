
import sys

def main():
    n, k, m = [int(i) for i in sys.stdin.readline().strip().split()]
    a = [int(i) for i in sys.stdin.readline().strip().split()]
    b = [int(i) for i in sys.stdin.readline().strip().split()]
    a_sum = sum(a)
    b_sum = sum(b)
    a_left = n
    b_left = n
    a_index = 0
    b_index = 0
    a_sum_segments = []
    b_sum_segments = []
    while a_index < n:
        if a_sum_segments == []:
            a_sum_segments.append(a[a_index])
        else:
            a_sum_segments.append(a_sum_segments[-1] + a[a_index])
        a_index += 1
    while b_index < n:
        if b_sum_segments == []:
            b_sum_segments.append(b[b_index])
        else:
            b_sum_segments.append(b_sum_segments[-1] + b[b_index])
        b_index += 1

    max_segments = []
    a_index = 0
    b_index = 0
    while a_index < n:
        if a_index + k < n:
            max_segments.append(a_sum_segments[a_index + k] - a_sum_segments[a_index])
        else:
            max_segments.append(a_sum_segments[n-1] - a_sum_segments[a_index])
        a_index += 1
    while b_index < n:
        if b_index + k < n:
            max_segments.append(b_sum_segments[b_index + k] - b_sum_segments[b_index])
        else:
            max_segments.append(b_sum_segments[n-1] - b_sum_segments[b_index])
        b_index += 1

    max_segments.sort(reverse=True)
    max_sum = 0
    m_index = 0
    while m_index < m:
        if m_index < len(max_segments):
            max_sum += max_segments[m_index]
        else:
            max_sum += 0
        m_index += 1
    print(max_sum)




































































































































































































































































































































































































































































































































































































































            else:
                break
        elif a_left == 0:
            if b_left > 0:
                b_left -= 1
                max_segments += 1
            else:
                break
        elif s[i] == 1:
            if a_left < a:
                a_left += 1
                b_left -= 1
                max_segments += 1
            elif b_left > 0:
                b_left -= 1
                max_segments += 1
            else:
                break
        elif s[i] == 0:
            if a_left > 0:
                a_left -= 1
                max_segments += 1
            elif b_left > 0:
                b_left -= 1
                max_segments += 1
            else:
                break
        i += 1
    print(max_segments)

main()
