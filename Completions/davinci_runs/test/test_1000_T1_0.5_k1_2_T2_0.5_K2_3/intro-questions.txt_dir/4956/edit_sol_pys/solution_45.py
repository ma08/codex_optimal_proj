

text = input().split()

count = 0
for word in text:
    if "ae" in word:
        count += 1
print(count)
print(len(text))
if count / len(text) > 0.4:
    print("dae ae ju traeligt va")  # dä ä ju träligt va
else:
    print("haer talar vi rikssvenska")  # här talar vi rikssvenska
