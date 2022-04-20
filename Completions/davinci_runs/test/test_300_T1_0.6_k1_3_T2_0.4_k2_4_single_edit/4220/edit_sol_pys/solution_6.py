

def file(k, s):
    if k > len(s):
        print(s)
    else:
        print(s[:k] + '...')


file(3, '123456789')
