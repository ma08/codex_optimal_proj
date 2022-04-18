

N, W, H = map(int, input().split()) # N = number of test cases, W = width, H = height

for _ in range(N):
    match = int(input()) # match = length of the matchstick
    if match <= (W**2 + H**2)**0.5: # checks if matchstick is smaller than the diagonal of the square
        print("DA") # if matchstick is smaller, print "DA"
    else:
        print("NE")
