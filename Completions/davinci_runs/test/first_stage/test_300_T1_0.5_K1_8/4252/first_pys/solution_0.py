

n = int(input())
s = input()

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

if len(list(find_all(s, "xxx"))) >= 1:
	print(len(list(find_all(s, "xxx"))))
else:
	print(0)