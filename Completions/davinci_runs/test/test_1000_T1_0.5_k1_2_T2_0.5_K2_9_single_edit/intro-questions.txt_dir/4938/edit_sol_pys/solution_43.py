

def main():
    i = 1
    for j in range(1, 10):
        for k in range(1, 10):
            print("{} * {} = {}".format(j, k, j*k))
            i += 1
            if i == 10:
                break
        if i == 10:
            break


if __name__ == "__main__":
    main()
