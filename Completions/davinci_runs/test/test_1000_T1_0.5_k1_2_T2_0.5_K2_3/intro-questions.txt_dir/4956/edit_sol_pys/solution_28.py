

def main():
    words = input().split()
    count = 0
    for word in words:
        if "ae" in word:
            count += 1
    if count >= len(words) * 0.4:
        print("dae ae ju traeligt va")  # "dae ae ju traeligt va" is a phrase from a swedish show called Swedish Dicks
    else:
        print("haer talar vi rikssvenska")  # "haer talar vi rikssvenska" means "here we speak Swedish"

main()
