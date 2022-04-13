
import sys

n = int(sys.stdin.readline())
words = sys.stdin.readline().split(" ")

if len(words) == n:
    count = 0
    for word in words:
        if word == "mumble":
            count += 1
        else:
            if int(word) != count + 1:
                print("something is fishy")
                sys.exit(0)
            else:
                count += 1
    if count == n:
        print("makes sense")
else:
    print("something is fishy")
