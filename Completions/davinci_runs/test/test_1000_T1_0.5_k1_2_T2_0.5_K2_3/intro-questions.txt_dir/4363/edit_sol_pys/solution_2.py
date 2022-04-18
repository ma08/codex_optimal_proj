

def main():
    k, s = map(int, input().split()) #mapでリストを作成, splitで区切る
    count = 0
    for x in range(k+1):
        for y in range(k+1):
            for z in range(k+1):
                if x + y + z == s:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()
