
import sys

def main():
    words = sys.stdin.readline().split()
    count = 0
    for word in words:
        if "a" in word:
            count += 1
    if count >= len(words) * 0.4:
        print("dae ae ju traeligt va") # då är du trött va
    else:
        print("haer talar vi rikssvenska") # här talar vi rikssvenska

if __name__ == '__main__':
    main()
