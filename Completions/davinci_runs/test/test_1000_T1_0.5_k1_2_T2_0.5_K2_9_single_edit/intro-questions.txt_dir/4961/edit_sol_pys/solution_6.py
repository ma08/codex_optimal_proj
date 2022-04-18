
def main():    
    S = raw_input()
    T = raw_input()
    S = S.lower()
    T = T.lower()
    if S == T:
        print 0
    elif S < T:
        print -1
    else:
        print 1
