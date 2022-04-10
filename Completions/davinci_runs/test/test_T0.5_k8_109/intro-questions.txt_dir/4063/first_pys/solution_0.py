

#def count_problems(N,d_lst,K):
#    count=0
#    for d in d_lst:
#        if d>=K:
#            count+=1
#    return count

#def main():
#    N=int(input())
#    d_lst=list(map(int,input().split()))
#    count=0
#    d_lst.sort()
#    if N%2==1:
#        print(0)
#        exit()
#    else:
#        for K in range(1,max(d_lst)+1):
#            if count_problems(N,d_lst,K)==N/2:
#                count+=1
#        print(count)

def main():
    N=int(input())
    d_lst=list(map(int,input().split()))
    d_lst.sort()
    count=0
    for i in range(N):
        if d_lst[i]==d_lst[N//2]:
            count+=1
    print(count)

if __name__=="__main__":
    main()