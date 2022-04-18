

for i in range(int(input())):
    n, k = map(int, input().split())
    if k*(k+1)//2 <= n:
        print("".join(map(chr, range(ord('a')+k-1, ord('a')-1, -1)))*(n//k) + "".join(map(chr, range(ord('a')+k-1, ord('a')-1, -1))[:n%k])
    else:
        print("".join(map(chr, range(ord('a'), ord('a')+k)))*(n//k) + "".join(map(chr, range(ord('a'), ord('a')+k)))[:n%k])