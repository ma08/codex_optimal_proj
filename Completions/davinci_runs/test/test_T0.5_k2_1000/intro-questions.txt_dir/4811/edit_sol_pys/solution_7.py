
import sys

def main():
    K = int(sys.stdin.readline().strip())
    print(find_bar_size(K), find_breaks(K)) 

def find_bar_size(k):
    bar_size = 1
    while bar_size < k:
        bar_size *= 2
    return bar_size

def find_breaks(k):
    bar_size = find_bar_size(k)
    breaks = 0
    while bar_size > k:
        bar_size /= 2
        breaks += 1
    return breaks

if __name__ == "__main__":
    main()
