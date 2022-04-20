

def main(inp, inp2):
    if inp[0] == inp2[0] and inp[1] == inp2[1]:
        return 0
    return 1

if __name__ == '__main__':
    inp2 = []
    inp = []
    for i in range(4):
        inp2.append(int(input()))
        inp.append(int(input()))
    print(main(inp))
