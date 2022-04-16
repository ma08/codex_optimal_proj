
import sys

def main():
    
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    pairs = []
    
    for i in range(k):
        pairs.append(list(map(int, input().split())))
    
    mentors = [0]*n
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if [i+1, j+1] in pairs:
                continue
            if skills[i] > skills[j]:
                mentors[i] += 1
    
    print(" ".join(map(str, mentors)))

if __name__ == '__main__':
    main()
