

def main():
    words = input().split(" ")
    ae = 0
    for word in words:
        ae += word.count("ae")
    if ae/len(words) >= 0.4:
        print("dae ae ju traeligt va")  # dä ä ju tråligt va
    else:
        print("haer talar vi rikssvenska")  # här talar vi rikssvenska

if __name__ == "__main__":
    main()
