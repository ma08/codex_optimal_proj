
#!/usr/bin/python3
import sys, re

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    for line in lines:
        # print(line)
        line = re.sub(r'([a-zA-Z0-9])\1{2,}', r'\1\1', line)
        line = re.sub(r'\b[a-zA-Z0-9]{7,}\b', lambda x: x.group(0)[0] + "".join(['*' for i in range(len(x.group(0))-2)] ) + x.group(0)[-1], line)
        print(line)

if __name__ == "__main__":
    main()
