

from sys import stdin, stdout

input = stdin.readline().strip()
output = ""

for i in range(len(input)):
    if input[i].isalpha():
        if input[i].isupper():
            output += (chr(ord(input[i]) + 32))
        else:
            output += input[i]
    else:
        output += input[i]

output = output.replace("a", "@")
output = output.replace("b", "8") 
output = output.replace("c", "(") 
output = output.replace("d", "|)") 
output = output.replace("e", "3") 
output = output.replace("f", "#") 
output = output.replace("g", "6") 
output = output.replace("h", "[-]") 
output = output.replace("i", "|") 
output = output.replace("j", "_|") 
output = output.replace("k", "|<") 
output = output.replace("l", "1") 
output = output.replace("m", "[]\/[]") 
output = output.replace("n", "[]\[]") 
output = output.replace("o", "0") 
output = output.replace("p", "|D") 
output = output.replace("q", "(,)") 
output = output.replace("r", "|Z") 
output = output.replace("s", "$") 
output = output.replace("t", "']['") 
output = output.replace("u", "|_|") 
output = output.replace("v", "\/") 
output = output.replace("w", "\/\/") 
output = output.replace("x", "}{") 
output = output.replace("y", "`/") 
output = output.replace("z", "2") 

stdout.write(output)
