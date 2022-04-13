
# https://codeforces.com/problemset/problem/1271/A

def main():
    # m, n = [int(x) for x in input().split()]
    # translations = {}
    # for i in range(m):
    #     a, b = input().split()
    #     translations[a] = b
    # for i in range(n):
    #     a, b = input().split()
    #     match = True
    #     if len(a) != len(b):
    #         match = False
    #     else:
    #         for j in range(len(a)):
    #             if a[j] not in translations and a[j] != b[j]:
    #                 match = False
    #                 break
    #             elif a[j] in translations and translations[a[j]] != b[j]:
    #                 match = False
    #                 break
    #     if match:
    #         print("yes")
    #     else:
    #         print("no")
    a = [1, 2, 3, 4, 5]
    b = a.copy()
    print(b)
    b[0] = 9
    print(b)
    print(a)

if __name__ == '__main__':
    main()
