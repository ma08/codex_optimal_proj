
n, m = map(int, input().split())

leftover = m - n

if leftover > 0:
    print("Dr. Chaz will have %d piece%s of chicken left over!" % (leftover, "s" if leftover != 1 else ""))
else:
    print("Dr. Chaz needs %d more piece%s of chicken!" % (-leftover, "s" if leftover != -1 else ""))
