

import sys

def main(filepath):
    with open(filepath, 'r') as f:
        n, k = map(int, f.readline().strip().split())
        s = f.readline().strip()

        # Calculate total cost of direct internet connection
        total_cost = 0
        for i in range(n):
            if s[i] == '0':
                total_cost += i + 1

        # Calculate minimum cost of router placement
        router_cost = 0
        for i in range(n):
            if s[i] == '1':
                router_cost += min(i + 1, n - i)
        
        # Calculate minimum cost of internet connection
        print(total_cost - router_cost)

if __name__ == '__main__':
    main(sys.argv[1])