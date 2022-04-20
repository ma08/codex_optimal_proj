

def main():
    N = int(input())
    S = set(input() for i in range(N))
    chars = set(['M', 'A', 'R', 'C', 'H'])
    count = 0
    for i in S:
        for j in S:
            for k in S:
                if i[0] in chars and j[0] in chars and k[0] in chars:
                    if len(set([i[0], j[0], k[0]])) == 3:
                        count += 1 
    print(count)

if __name__ == '__main__':
    main()
