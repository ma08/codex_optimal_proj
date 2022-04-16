

from sys import stdin, stdout

input_string = stdin.readline().strip()
output_string = ""

for i in range(len(input_string)):
    if input_string[i].isalpha():
        if input_string[i].isupper():
            output_string += (chr(ord(input_string[i]) + 32))
        else:
            output_string += input_string[i]
    else:
        output_string += input_string[i]

output_string = output_string.replace("a", "@")
output_string = output_string.replace("b", "8")
output_string = output_string.replace("c", "(")
output_string = output_string.replace("d", "|)")
output_string = output_string.replace("e", "3")
output_string = output_string.replace("f", "#")
output_string = output_string.replace("g", "6")
output_string = output_string.replace("h", "[-]")
output_string = output_string.replace("i", "|")
output_string = output_string.replace("j", "_|")
output_string = output_string.replace("k", "|<")
output_string = output_string.replace("l", "1")
output_string = output_string.replace("m", "[]\/[]")
output_string = output_string.replace("n", "[]\[]")
output_string = output_string.replace("o", "0")
output_string = output_string.replace("p", "|D")
output_string = output_string.replace("q", "(,)")
output_string = output_string.replace("r", "|Z")
output_string = output_string.replace("s", "$")
output_string = output_string.replace("t", "']['")
output_string = output_string.replace("u", "|_|")
output_string = output_string.replace("v", "\/")
output_string = output_string.replace("w", "\/\/")
output_string = output_string.replace("x", "}{")
output_string = output_string.replace("y", "`/")
output_string = output_string.replace("z", "2")

stdout.write(output_string)
