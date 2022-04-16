
import sys

def main():
    n = int(sys.stdin.readline())
    dirty_pushes = [int(x) for x in sys.stdin.readline().split()]
    total_dirtiness = 0
    cleanup_phases = 0
    for i in range(n):
        total_dirtiness += (dirty_pushes[i] - i)
        if total_dirtiness >= 20:
            cleanup_phases += 1
            total_dirtiness = 0
    print(cleanup_phases)

if __name__ == "__main__":
    main()
