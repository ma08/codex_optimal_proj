
n = int(input())
recited_numbers = []

for i in range(n):
    recited_numbers.append(int(input()))

for i in range(1, recited_numbers[-1] + 1):
    if i not in recited_numbers:
        print(i)

if len(recited_numbers) == recited_numbers[-1]:
    print("good job")
