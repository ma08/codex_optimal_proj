

import sys

def main():
    expr = input()
    tokens = expr.split("+")
    for i in range(len(tokens)):
        token = tokens[i]
        if "-" in token:
            tokens[i] = token.split("-")

    print("".join("+" * int(t) for t in tokens[0]))
    for token in tokens[1:]:
        print("".join("+" * int(t) for t in token[:-1]))
        print("".join("-" * int(t) for t in token[-1:]))
    print("<[<+>-]<" * len(tokens))
    print("+" * 255)
    print(".")

if __name__ == "__main__":
    main()