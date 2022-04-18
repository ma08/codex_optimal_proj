

def main():
    wall_len = int(input())
    wall_cond = list(input())
    for i in range(wall_len):
        if wall_cond[i] == '1':
            for j in range(i, wall_len):
                if wall_cond[j] == '0':
                    wall_cond[j] = '1'
                else:
                    wall_cond[j] = '0'
    print(wall_cond.count('0'))


if __name__ == "__main__":
    main()
