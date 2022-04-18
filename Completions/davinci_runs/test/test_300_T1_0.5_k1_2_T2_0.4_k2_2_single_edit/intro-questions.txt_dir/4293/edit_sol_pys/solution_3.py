
import sys

def main(P, Q, R):
    return min(P+Q, Q+R, R+P)

if __name__ == "__main__":
    main()
