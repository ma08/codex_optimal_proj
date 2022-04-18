

def find_blocks(l):
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return 1
    else:
        total = sum(l)
        if total % 2 == 0:
            possible_total = total / 2
            left = 0
            right = len(l) - 1
            while left != right:
                if l[left] > possible_total:
                    return 0
                elif l[left] == possible_total:
                    return 1
                elif sum(l[left:right]) == possible_total:
                    return 2
                elif sum(l[left:right]) < possible_total:
                    left += 1
                else:
                    right -= 1
            return 0
        else:
            return 0


def main():
    n = input()
    l = map(int, raw_input().split())
    blocks = []
    for i in range(n):
        for j in range(i, n):
            result = find_blocks(l[i:j])
            if result == 2:
                blocks.append([i, j])
    print len(blocks)
    for i in blocks:
        print i[0] + 1, i[1] + 1

main()
