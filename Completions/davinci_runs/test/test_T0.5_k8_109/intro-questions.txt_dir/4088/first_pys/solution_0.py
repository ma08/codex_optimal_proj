

import random

def gen_test_cases(q):
    for i in range(q):
        s = ""
        for j in range(random.randint(1,50)):
            s += chr(random.randint(97,122))
        m = random.randint(1,len(s))
        b = []
        for j in range(m):
            b.append(random.randint(0,1225))
        print(s)
        print(m)
        print(" ".join(str(k) for k in b))

if __name__ == "__main__":
    gen_test_cases(4)