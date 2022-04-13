
import sys

def main():
    words = sys.stdin.readlines()
    ae_count = 0
    word_count = 0
    for line in words:
        for word in line.split():
            word_count += 1
            for letter in word:
                if letter == 'a' or letter == 'e':
                    ae_count += 1
    if ae_count / word_count >= 0.4:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")

if __name__ == '__main__':
    main()
