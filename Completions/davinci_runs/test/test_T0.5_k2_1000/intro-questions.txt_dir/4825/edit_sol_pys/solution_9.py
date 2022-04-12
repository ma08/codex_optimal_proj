
import sys

def main():
    text = sys.stdin.readline().strip()

    text = text.replace("a", "@")
    text = text.replace("b", "8")
    text = text.replace("c", "(")
    text = text.replace("d", "|)")
    text = text.replace("e", "3")
    text = text.replace("f", "#")
    text = text.replace("g", "6")
    text = text.replace("h", "[-]")
    text = text.replace("i", "|")
    text = text.replace("j", "_|")
    text = text.replace("k", "|<")
    text = text.replace("l", "1")
    text = text.replace("m", "[]\\/[]")
    text = text.replace("n", "[]\\[]")
    text = text.replace("o", "0")
    text = text.replace("p", "|D")
    text = text.replace("q", "(,)")
    text = text.replace("r", "|Z")
    text = text.replace("s", "$")
    text = text.replace("t", "7")
    text = text.replace("u", "|_|")
    text = text.replace("v", "\\/")
    text = text.replace("w", "\\/\\/")
    text = text.replace("x", "}{}")
    text = text.replace("y", "`/")
    text = text.replace("z", "2")
    print(text)

if __name__ == '__main__':
    main()
