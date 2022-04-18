

def simplicity(s_):
    return len(set(s_))

def min_erase(s_):
    min_erase = len(s_)
    for i in range(len(s_)):
        _s = s_[:i] + s_[i+1:]
        min_erase = min(min_erase, len(s_) - simplicity(_s))
    return min_erase

if __name__ == '__main__':
    print(min_erase(input()))
