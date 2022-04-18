

if __name__ == '__main__':
    S = input()
    if len(S) == len(set(S)):  # set()で集合にすると重複を無くす
        print("yes")
    else:
        print("no")
