
input = open("input.txt", "r")
output = open("output.txt", "w")
a, b = input.readline().split()
a, b = int(a), int(b)
c = a + b
output.write(str(c))
input.close()
output.close()
