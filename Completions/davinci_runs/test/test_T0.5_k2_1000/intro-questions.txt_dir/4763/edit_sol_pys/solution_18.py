
import sys

def main():
    n = int(sys.stdin.readline())

    if n <= 60:
        print("impossible")
        return

    # Find the largest number of triples that can be used
    num_triples = n // 60
    num_triples = min(num_triples, 3)
    n -= num_triples*60

    # Find the largest number of doubles that can be used
    num_doubles = n // 30
    num_doubles = min(num_doubles, 3-num_triples)
    n -= num_doubles*30

    # Find the largest number of singles that can be used
    num_singles = n // 10
    num_singles = min(num_singles, 3-num_triples-num_doubles)
    n -= num_singles*10

    if n > 0:
        print("impossible")
        return

    for i in range(num_triples):
        print("triple 20") 
    for i in range(num_doubles):
        print("double 20")
    for i in range(num_singles):
        print("single 20")

if __name__ == '__main__':
    main()
