

def main():
    words = input().split(" ")
    count = 0
    for word in words:
        if "ae" in word:
            count += 1
    if count >= len(words) // 5:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")

main()
