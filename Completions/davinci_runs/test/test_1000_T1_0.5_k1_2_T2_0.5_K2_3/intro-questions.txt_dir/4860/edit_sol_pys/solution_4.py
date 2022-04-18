
n = int(input("Enter a number: "))
recited_numbers = [1, 2, 4, 5, 7]

for i in range(n + 1):
    if i not in recited_numbers:
        print(i)
        break

if len(recited_numbers) == n:
    print("good job")
