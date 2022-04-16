

N, M = [int(x) for x in input().split()] #N is the number of people and M is the number of chicken legs

if N > M:
    print("Dr. Chaz needs {} more piece[s] of chicken!".format(N - M)) #if N is greater than M, then it will print the number of chicken legs that Dr. Chaz needs
else:
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(M - N)) #if M is greater than N, then it will print the number of chicken legs that Dr. Chaz will have left over
