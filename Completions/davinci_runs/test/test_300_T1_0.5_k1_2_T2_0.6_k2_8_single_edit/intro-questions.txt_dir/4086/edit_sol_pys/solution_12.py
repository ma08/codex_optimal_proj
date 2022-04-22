import sys
import os
import hashlib


def file_hash(filename):
    h = hashlib.sha1()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def remove_duplicates(a):
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    return b

b = remove_duplicates(a)
print(len(b))
print(*b)
