
for i in range(int(input())):
    n = int(input())
    s = input()
    l = len(s)
    s = s.replace("I", "1").replace("O", "0")
    print(int(s, 2))
