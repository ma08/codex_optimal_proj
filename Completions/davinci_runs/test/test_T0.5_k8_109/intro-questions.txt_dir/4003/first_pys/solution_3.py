

#-----Solution-----

def main():
    n = int(input())
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    left = lst[:]
    right = lst[:]
    left_max = 0
    right_max = 0
    left_lst = []
    right_lst = []
    for i in range(n):
        if left_max <= left[0]:
            left_max = left[0]
            left_lst.append(left[0])
            del left[0]
        else:
            del left[0]
        if right_max <= right[-1]:
            right_max = right[-1]
            right_lst.append(right[-1])
            del right[-1]
        else:
            del right[-1]
    if len(left_lst) > len(right_lst):
        print(len(left_lst))
        print('L' * len(left_lst))
    else:
        print(len(right_lst))
        print('R' * len(right_lst))

main()