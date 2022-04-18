import os


def get_files(path):
    files = os.listdir(path)
    for file in files:
        print(file)

def main():
    get_files("/Users/yana/Downloads/")

segments.sort(key=lambda x: x[0])

# print(segments)

res = []
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments] and i not in [seg[1] for seg in segments]:
        res.append(i)

print(len(res))
print(*res)
