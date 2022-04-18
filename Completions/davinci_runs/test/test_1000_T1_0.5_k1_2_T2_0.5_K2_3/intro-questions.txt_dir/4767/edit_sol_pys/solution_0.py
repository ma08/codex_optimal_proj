
import sys

def main():
    count = 0
    regs = [0] * 20
    while True:
        regs[0] += 1
        if regs[0] == 20:
            regs[0] = 0
            regs[1] += 1
            if regs[1] == 20:
                regs[1] = 0
                regs[2] += 1
                if regs[2] == 20:
                    regs[2] = 0
                    regs[3] += 1
                    if regs[3] == 20:
                        regs[3] = 0
                        regs[4] += 1
                        if regs[4] == 20:
                            regs[4] = 0
                            regs[5] += 1
                            if regs[5] == 20:
                                regs[5] = 0
                                regs[6] += 1
                                if regs[6] == 20:
                                    regs[6] = 0
                                    regs[7] += 1
                                    if regs[7] == 20:
                                        regs[7] = 0
                                        regs[8] += 1
                                        if regs[8] == 20:
                                            regs[8] = 0
                                            regs[9] += 1
                                            if regs[9] == 20:
                                                regs[9] = 0
                                                regs[10] += 1
                                                if regs[10] == 20:
                                                    regs[10] = 0
                                                    regs[11] += 1
                                                    if regs[11] == 20:
                                                        regs[11] = 0
                                                        regs[12] += 1
                                                        if regs[12] == 20:
                                                            regs[12] = 0
                                                            regs[13] += 1
                                                            if regs[13] == 20:
                                                                regs[13] = 0
                                                                regs[14] += 1
                                                                if regs[14] == 20:
                                                                    regs[14] = 0
                                                                    regs[15] += 1
                                                                    if regs[15] == 20:
                                                                        regs[15] = 0
                                                                        regs[16] += 1
                                                                        if regs[16] == 20:
                                                                            regs[16] = 0
                                                                            regs[17] += 1
                                                                            if regs[17] == 20:
                                                                                regs[17] = 0
                                                                                regs[18] += 1
                                                                                if regs[18] == 20:
                                                                                    regs[18] = 0
                                                                                    regs[19] += 1
                                                                                    if regs[19] == 20:
                                                                                        regs[19] = 0
                                                                                        break
        count += 1

    print(count)

if __name__ == '__main__':
    main()
