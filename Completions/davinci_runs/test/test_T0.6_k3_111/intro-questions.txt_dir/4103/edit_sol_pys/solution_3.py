
import numpy as np

def main():
    n, b, a = [int(x) for x in input().split()] # n = number of switches, b = number of batteries, a = number of adapters
    s = [int(x) for x in input().split()] # s = list of switches
    s = np.array(s)
    b_curr, a_curr = b, a # b_curr = current number of batteries, a_curr = current number of adapters
    i = 0
    while i < n:
        if s[i] == 1: # if the switch is on
            if a_curr < a: # if there are less adapters than the maximum
                a_curr += 1
            else: # if there are more adapters than the maximum
                b_curr += 1
            i += 1
        elif s[i] == 0: # if the switch is off
            if b_curr > 0: # if there are batteries
                b_curr -= 1
                i += 1
            elif a_curr > 0: # if there are adapters
                a_curr -= 1
                i += 1
            else: # if there are no batteries or adapters
                break
    print(i)

if __name__ == "__main__":
    main()
