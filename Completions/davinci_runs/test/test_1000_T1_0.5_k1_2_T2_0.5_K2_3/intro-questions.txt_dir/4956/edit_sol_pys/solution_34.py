

def main():
    words = input("Enter a sentence: ").split()
    count = 0
    for word in words:
        if "ae" in word:
            count += 1
    if count >= len(words) * 0.4:
        print("dae ae ju traeligt va", end="")
    else:
        print("haer talar vi rikssvenska", end="") 

main()
