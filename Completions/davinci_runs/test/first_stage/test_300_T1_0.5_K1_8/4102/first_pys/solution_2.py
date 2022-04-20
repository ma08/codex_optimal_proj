

#Solution

def is_lucky(n):
    if sum(map(int, n[:len(n)//2])) == sum(map(int, n[len(n)//2:])) :
        return 'Yes'
    else :
        return 'No'

#Test

print(is_lucky(input()))