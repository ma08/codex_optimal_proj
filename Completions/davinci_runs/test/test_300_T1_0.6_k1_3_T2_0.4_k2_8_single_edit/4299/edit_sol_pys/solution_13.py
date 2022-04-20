
N = int(input())
N_list = list(str(N))
N_last = int(N_list[-1])

if N_last == 2 or N_last == 4 or N_last == 5 or N_last == 7 or N_last == 9:
    print('hon')

elif N_last == 0 or N_last == 1 or N_last == 6 or N_last == 8:
    print('pon')

else:
    print('bon')
