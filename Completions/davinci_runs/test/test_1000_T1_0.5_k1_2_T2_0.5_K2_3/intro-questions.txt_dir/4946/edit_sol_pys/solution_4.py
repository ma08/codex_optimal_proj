# This is the solution for Stacks and Queues > Fish
#
# This is marked as RESPECTABLE difficulty


def solution(A, B):
    count = 0
    stack = []
    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while len(stack) > 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                count += 1
    return count + len(stack)

if __name__ == '__main__':
    print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
