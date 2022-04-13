
import sys

def main():
    K = int(sys.stdin.readline().strip())
    print(find_bar_size(K), find_break(K), sep=' ')

def find_bar_size(k):
    bar_size = 1
    while bar_size < k:
        bar_size *= 2
    return bar_size

def find_break(k):
    bar_size = find_bar_size(k)
    break_ = 0
    while bar_size > k:
        bar_size /= 2
        break_ += 1
    return break_

if __name__ == "__main__":
    main()
