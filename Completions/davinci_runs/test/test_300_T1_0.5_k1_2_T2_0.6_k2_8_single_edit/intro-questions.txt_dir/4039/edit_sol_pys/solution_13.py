import argparse


def main(args):
    print("Hello World")
    print(args.filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    main(args)
