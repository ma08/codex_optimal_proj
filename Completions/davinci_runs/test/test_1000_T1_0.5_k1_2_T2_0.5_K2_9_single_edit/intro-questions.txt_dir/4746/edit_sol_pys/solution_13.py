
import sys, math
 
def main():    
    n = int(sys.stdin.readline())
    for i in range(n):
        num = int(sys.stdin.readline())
        if num == 1:
            print("1")
        elif num == 4:
            print("2")
        else:
            print("3")
 
if __name__ == "__main__":
    main() 
