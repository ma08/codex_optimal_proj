

import sys, os

print(os.listdir())
print(os.getcwd())

f = open('test.txt', 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

f = open('test.txt', 'r')
line = f.readline()
print(line)
f.close()

f = open('test.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('test.txt', 'r')
data = f.read()
print(data)
f.close()

f = open('test.txt', 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

with open('test.txt', 'r') as f:
    data = f.read()
    print(data)
