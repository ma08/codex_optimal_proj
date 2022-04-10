
import sys

def main():
    num_cases = int(sys.stdin.readline())
    for i in range(num_cases):
        s = list(sys.stdin.readline().strip())
        m = int(sys.stdin.readline().strip())
        b = [int(i) for i in sys.stdin.readline().strip().split()]
        #print(s,m,b)
        t = []
        for i in range(len(b)):
            curr_char = s[i]
            curr_b = b[i]
            for j in range(26):
                if chr(ord('a') + j) > curr_char:
                    curr_b -= abs(ord(curr_char) - ord('a') - j)
            t.append(chr(ord('a') + curr_b))
        print(''.join(t))

if __name__ == "__main__":
    main()