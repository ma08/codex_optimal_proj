

def main():
    d, g = map(int, input().split())
    p_c_list = [list(map(int, input().split())) for i in range(d)]
    ans = 10**7
    for i in range(2**d):
        count = 0
        bonus = 0
        remainder = g
        for j in range(d):
            if (i >> j) & 1:
                count += p_c_list[j][0]
                bonus += p_c_list[j][1]
            else:
                remainder -= (j+1)*100*p_c_list[j][0] + p_c_list[j][1]
        if remainder <= 0:
            ans = min(ans, count)
        else:
            for j in range(d):
                if not ((i >> j) & 1):
                    if remainder <= (j+1)*100*(p_c_list[j][0]-1):
                        count += remainder//((j+1)*100)
                        ans = min(ans, count)
                        break
                    else:
                        count += p_c_list[j][0]
                        bonus += p_c_list[j][1]
                        remainder -= (j+1)*100*p_c_list[j][0]
    print(ans)

if __name__ == '__main__':
    main()
