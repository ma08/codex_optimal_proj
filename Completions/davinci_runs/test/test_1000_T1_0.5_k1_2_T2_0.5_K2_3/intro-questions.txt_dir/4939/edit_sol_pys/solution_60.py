
n, k = map(int, input().split())  # n - number of students, k - number of throws
throws = input().split()

current_student = 0  # current student
current_throw = 0  # current throw

while current_throw < k:  # while current throw is less than total number of throws
    if throws[current_throw].isdigit():  # if current throw is digit
        current_student = (current_student + int(throws[current_throw]) % n) % n  # add to current student
        current_throw += 1  # increase current throw
    else:
        m = int(throws[current_throw][5:])  # if current throw is not digit
        for _ in range(m):  # add to current student
            current_throw -= 1  # decrease current throw
            if throws[current_throw].isdigit():  # if current throw is digit
                current_student = (current_student - int(throws[current_throw]) % n) % n  # subtract from current student
            else:
                m = int(throws[current_throw][5:])  # if current throw is not digit
                for _ in range(m):  # subtract from current student
                    current_throw -= 1  # decrease current throw
                    current_student = (current_student + int(throws[current_throw]) % n) % n  # add to current student

print(current_student)
