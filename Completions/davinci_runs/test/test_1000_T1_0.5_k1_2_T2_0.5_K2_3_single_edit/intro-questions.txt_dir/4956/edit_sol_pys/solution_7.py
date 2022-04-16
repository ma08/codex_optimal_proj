
text = input().split()

count = 0
for word in text:
    if "ae" in word:
        count += 1

if count / len(text) > 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
