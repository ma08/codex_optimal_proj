
import argparse
# TODO: implement the solution

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    print(args.filename)
    with open(args.filename) as f:
        for line in f:
            print(line, end="")

if __name__ == "__main__":
    main()
