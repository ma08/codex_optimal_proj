
import sys

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)] # read all the lines
    dic = {}
    for name in names: # count the number of names that start with each letter
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
    keys = dic.keys() # get all the letters
    ans = 0
    for i in range(len(keys)): # for each triplet of letters
        for j in range(i+1, len(keys)):
            for k in range(j+1, len(keys)):
                ans += dic[keys[i]] * dic[keys[j]] * dic[keys[k]] # multiply the number of names that start with each letter
    print(ans)


if __name__ == '__main__':
    main()
