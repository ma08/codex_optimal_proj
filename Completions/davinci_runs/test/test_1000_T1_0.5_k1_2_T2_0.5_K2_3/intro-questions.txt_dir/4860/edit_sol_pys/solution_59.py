
n = int(input())
list_of_recited_numbers = []

for i in range(n):
    list_of_recited_numbers.append(int(input()))

for i in range(1, list_of_recited_numbers[-1] + 1):
    if i not in list_of_recited_numbers:
        print(i)

if len(list_of_recited_numbers) == list_of_recited_numbers[-1]:
    print("good job")
