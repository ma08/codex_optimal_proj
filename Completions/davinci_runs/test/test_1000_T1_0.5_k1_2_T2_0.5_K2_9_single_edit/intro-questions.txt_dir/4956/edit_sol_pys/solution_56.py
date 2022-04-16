
import sys, random

def main():
    lines = sys.stdin.readlines()
    words = [word.strip() for line in lines for word in line.split()]
    print(words)
    # count = 0
    # for word in words:
    #     if "ae" in word:
    #         count += 1
    # if count >= len(words) * 0.4:
    #     print("dae ae ju traeligt va")
    # else:
    #     print("haer talar vi rikssvenska")

if __name__ == '__main__':
    main()
