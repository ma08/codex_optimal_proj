
import sys
import math

def main():
    words = sys.stdin.readline().lower()
    ae_count = 0
    word_count = 0
    for word in words.split():
        word_count += 1
        if "ae" in word:
            ae_count += 1
    if ae_count/word_count >= 0.4:
        print("dae ae ju traeligt va") 
    else:
        print("haer talar vi rikssvenska") 

if __name__ == '__main__':
    main()
