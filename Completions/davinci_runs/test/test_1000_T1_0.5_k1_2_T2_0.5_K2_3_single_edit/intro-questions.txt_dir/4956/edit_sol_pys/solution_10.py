
import sys

def main():
    words = sys.stdin.readline().split()
    count = 0
    for word in words:
        if "ae" in word:
            count += 1
    if count >= len(words) * 0.4:
        print("dae ae ju traeligt va")  # the correct spelling is dä ä ju tråligt va
    else:
        print("haer talar vi rikssvenska")  # the correct spelling is här talar vi rikssvenska

if __name__ == '__main__':
    main()
