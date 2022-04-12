

def main():
    n, m = map(int, input().split())
    translations = {}
    for i in range(m):
        a, b = input().split()
        translations[a] = b
    for i in range(n):
        a, b = map(str, input().split())
        match = True
        if len(a) != len(b):
            match = False
        else:
            for j in range(len(a)):
                if a[j] not in translations and a[j] != b[j]:
                    match = False
                    break
                elif a[j] in translations and translations[a[j]] != b[j]:
                    match = False
                    break
        if match:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    main()
