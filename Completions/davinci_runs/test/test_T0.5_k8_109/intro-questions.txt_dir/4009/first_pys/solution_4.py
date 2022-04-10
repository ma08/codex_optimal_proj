

#-----Solution-----

def get_number(number, x, y):
    #number = [int(i) for i in number]
    #print(number)
    number = [int(i) for i in number]
    #print(number)
    answer = 0
    for i in range(len(number) - 1, -1, -1):
        if i >= x:
            if number[i] == 1:
                answer += 1
                number[i] = 0
        elif i >= y:
            if number[i] == 0:
                answer += 1
                number[i] = 1
        else:
            if number[i] == 1:
                answer += 1
                number[i] = 0
    return answer

n, x, y = input().split()
n, x, y = int(n), int(x), int(y)
number = input()

print(get_number(number, x, y))