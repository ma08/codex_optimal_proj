
N = int(input())
N_list = list(str(N))
N_list[-1] = int(N_list[-1]) 

if N_list[-1] == 2 or N_list[-1] == 4 or N_list[-1] == 5 or N_list[-1] == 7 or N_list[-1] == 9:
    print('hon')

elif N_list[-1] == 0 or N_list[-1] == 1 or N_list[-1] == 6 or N_list[-1] == 8:
    print('pon')

else:
    print('bon')
