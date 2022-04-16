

from collections import defaultdict

def main(): 
    d = defaultdict(int) 
    for i in range(int(input())): 
        word = input() 
        d[word] += 1 
    print(len(d)) 
    print(*d.values()) 
main() 
