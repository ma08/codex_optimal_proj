
N = int(input())
N_list = list(str(N))
N_list[-1] = int(N_list[-1]) # 文字列をintに変換

if N_list[-1] in [2, 4, 5, 7, 9]:
    print('hon')

elif N_list[-1] in [0, 1, 6, 8]:
    print('pon')

else:
    print('bon')
