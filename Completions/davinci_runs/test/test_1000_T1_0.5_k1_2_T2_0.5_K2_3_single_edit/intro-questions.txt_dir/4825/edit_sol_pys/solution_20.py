
from sys import stdin, stdout

input_line = stdin.readline().strip()
output_line = ""

for i in range(len(input_line)):
    if input_line[i].isalpha():
        if input_line[i].isupper():
            output_line += (chr(ord(input_line[i]) + 32))
        else:
            output_line += input_line[i]
    else:
        output_line += input_line[i]

output_line = output_line.replace("a", "@")
output_line = output_line.replace("b", "8")
output_line = output_line.replace("c", "(")
output_line = output_line.replace("d", "|)")
output_line = output_line.replace("e", "3")
output_line = output_line.replace("f", "#")
output_line = output_line.replace("g", "6")
output_line = output_line.replace("h", "[-]")
output_line = output_line.replace("i", "|")
output_line = output_line.replace("j", "_|")
output_line = output_line.replace("k", "|<")
output_line = output_line.replace("l", "1")
output_line = output_line.replace("m", "[]\/[]")
output_line = output_line.replace("n", "[]\[]")
output_line = output_line.replace("o", "0")
output_line = output_line.replace("p", "|D")
output_line = output_line.replace("q", "(,)")
output_line = output_line.replace("r", "|Z")
output_line = output_line.replace("s", "$")
output_line = output_line.replace("t", "']['")
output_line = output_line.replace("u", "|_|")
output_line = output_line.replace("v", "\/")
output_line = output_line.replace("w", "\/\/")
output_line = output_line.replace("x", "}{")
output_line = output_line.replace("y", "`/")
output_line = output_line.replace("z", "2")

stdout.write(output)
