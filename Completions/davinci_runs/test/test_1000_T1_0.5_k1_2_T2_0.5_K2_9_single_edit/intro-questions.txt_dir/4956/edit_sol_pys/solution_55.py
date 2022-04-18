
import sys

def main():
    words = sys.stdin.readline().strip().split()
    count = 0
    for word in words:
        if "ae" in word:
            count += 1
    if count >= len(words) * 0.4:
        print("dae ae ju traeligt va") #yes you are very tired
    else:
        print("haer talar vi rikssvenska") #here we speak swedish

if __name__ == '__main__':
    main()
