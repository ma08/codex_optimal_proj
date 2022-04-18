import sys

def main():
    N = int(sys.stdin.readline())
    costumes = set()
    for _ in range(N):
        costumes.add(sys.stdin.readline().strip())
    
    costumes = list(costumes)
    costumes.sort()
    for costume in costumes:
        print(costume)
    
if __name__ == "__main__":
    main()
