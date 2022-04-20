
import math

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # print(N,A,B,C,D,E)
    # print(math.ceil(N/A))
    # print(math.ceil(N/B))
    # print(math.ceil(N/C))
    # print(math.ceil(N/D))
    # print(math.ceil(N/E))
    print(max(math.ceil(N/A),math.ceil(N/B),math.ceil(N/C),math.ceil(N/D),math.ceil(N/E)))

if __name__ == '__main__':
    main()