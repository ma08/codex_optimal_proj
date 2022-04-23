#!/usr/bin/python

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        return 1
    filename = sys.argv[1]

    # read file
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    print(content)

    # parse file
    data = {}
    for line in content:
        if ":" not in line:
            continue
        key, val = line.split(":")
        data[key] = val
    print(data)

    # write file
    with open(filename, "w") as f:
        for k, v in data.items():
            f.write("%s:%s\n" % (k, v))

if __name__ == "__main__":
    main()
