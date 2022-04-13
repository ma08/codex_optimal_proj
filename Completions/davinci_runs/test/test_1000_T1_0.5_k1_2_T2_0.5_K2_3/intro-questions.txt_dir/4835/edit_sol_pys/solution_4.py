

import sys

def main():
    
    if dist[0][0] != -1 and dist[0][0] <= t:
        print(dist[0][0])
    elif dist[0][M-1] != -1 and dist[0][M-1] <= t:
        print(dist[0][M-1])
    elif dist[N-1][0] != -1 and dist[N-1][0] <= t:
        print(dist[N-1][0])
    elif dist[N-1][M-1] != -1 and dist[N-1][M-1] <= t:
        print(dist[N-1][M-1])
    else:
        print('NOT POSSIBLE')


if __name__ == '__main__':
    main()
