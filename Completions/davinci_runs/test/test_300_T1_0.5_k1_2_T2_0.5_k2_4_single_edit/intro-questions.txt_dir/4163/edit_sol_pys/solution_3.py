def main():
    s = input()
    cnt = 0
    for c in s:
        if c == 'o':
            cnt += 1
    print('o' * cnt + 'k' * (15 - cnt))



if __name__ == '__main__':
    main()
