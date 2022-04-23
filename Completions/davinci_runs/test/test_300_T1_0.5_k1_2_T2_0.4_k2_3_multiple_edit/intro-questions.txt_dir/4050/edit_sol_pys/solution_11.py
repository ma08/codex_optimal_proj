

def find_blocks(a, s):
    n = len(a) 
    d = {} 
    for i in range(n): 
        for j in range(i, n): 
            sum_ = sum(a[i:j+1]) 
            if sum_ not in d: 
                d[sum_] = [(i, j)] 
            else: 
                d[sum_].append((i, j)) 
    res = [] 
    for i in range(n): 
        for j in range(i, n): 
            sum_ = sum(a[i:j+1]) 
            if sum_ in d: 
                for l, r in d[sum_]: 
                    if l > j or r < i: 
                        if sum_ == s: 
                            res.append((i, j)) 
    return res 

def main():
    n = int(input("Enter the number of elements: ")) 
    a = [int(s) for s in input("Enter the elements: ").split()] 
    s = int(input("Enter the sum: ")) 
    res = find_blocks(a, s) 
    print(len(res)) 
    for l, r in res: 
        print(l+1, r+1) 

if __name__ == "__main__": 
    main() 
