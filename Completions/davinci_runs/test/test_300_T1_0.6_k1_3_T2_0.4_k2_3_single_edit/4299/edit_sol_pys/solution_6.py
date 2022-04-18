
N = int(input())
N_list = list(str(N))
N_list = int(N_list[-1])

if N_list == 2 or N_list == 4 or N_list == 5 or N_list == 7 or N_list == 9:
    print('hon')

elif N_list == 0 or N_list == 1 or N_list == 6 or N_list == 8:
    print('pon')

else:
    print('bon')
