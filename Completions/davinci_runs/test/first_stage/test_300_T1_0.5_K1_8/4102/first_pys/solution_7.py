

def is_lucky(number):
    if len(number)%2 != 0:
        return 'No'
    half = len(number)//2
    first_half = sum(int(i) for i in number[:half])
    second_half = sum(int(i) for i in number[half:])
    if first_half == second_half:
        return 'Yes'
    else:
        return 'No'

print(is_lucky(input()))