
binar = input()
binar = binar[::-1]
binar = binar + (3 - len(binar) % 3) * '0' # if len(binar) % 3 <> 0
octl = ''
for i in range(0, len(binar), 3):
    octl += str(int(binar[i:i + 3], 2))

print(int(octl[::-1]))
