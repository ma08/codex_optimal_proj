

def main():
    # Read input
    sentence = input()

    # Split sentence into words and count
    words = sentence.split()
    num_words = len(words)

    # Count number of words with å
    num_å = 0
    for word in words:
        if "å" in word:
            num_å += 1

    # Print correct output
    if num_å/num_words >= 0.4:
        print("då å ju tråligt va")
    else:
        print("här talar vi rikssvenska")


if __name__ == "__main__":
    main()
