

N, M = map(int, input().split())

s_list = []
c_list = []

for i in range(M):
    s, c = map(int, input().split())
    s_list.append(s)
    c_list.append(c)


if N == 1:
    if 1 in s_list:
        print(c_list[s_list.index(1)])
    else:
        print(-1)

elif N == 2:
    if 1 in s_list:
        if 2 in s_list:
            print(str(c_list[s_list.index(1)]) + str(c_list[s_list.index(2)]))
        else:
            if c_list[s_list.index(1)] == 0:
                print(-1)
            else:
                print(str(c_list[s_list.index(1)]) + "0")
    else:
        if 2 in s_list:
            if c_list[s_list.index(2)] == 0:
                print(-1)
            else:
                print("0" + str(c_list[s_list.index(2)]))
        else:
            print("00")

elif N == 3:
    if 1 in s_list:
        if 2 in s_list:
            if 3 in s_list:
                print(str(c_list[s_list.index(1)]) + str(c_list[s_list.index(2)]) + str(c_list[s_list.index(3)]))
            else:
                if c_list[s_list.index(1)] == 0:
                    print(-1)
                else:
                    print(str(c_list[s_list.index(1)]) + str(c_list[s_list.index(2)]) + "0")
        else:
            if 3 in s_list:
                if c_list[s_list.index(1)] == 0:
                    print(-1)
                else:
                    print(str(c_list[s_list.index(1)]) + "0" + str(c_list[s_list.index(3)]))
            else:
                if c_list[s_list.index(1)] == 0:
                    print(-1)
                else:
                    print(str(c_list[s_list.index(1)]) + "00")
    else:
        if 2 in s_list:
            if 3 in s_list:
                if c_list[s_list.index(2)] == 0:
                    print(-1)
                else:
                    print("0" + str(c_list[s_list.index(2)]) + str(c_list[s_list.index(3)]))
            else:
                if c_list[s_list.index(2)] == 0:
                    print(-1)
                else:
                    print("0" + str(c_list[s_list.index(2)]) + "0")
        else:
            if 3 in s_list:
                if c_list[s_list.index(3)] == 0:
                    print(-1)
                else:
                    print("00" + str(c_list[s_list.index(3)]))
            else:
                print("000")