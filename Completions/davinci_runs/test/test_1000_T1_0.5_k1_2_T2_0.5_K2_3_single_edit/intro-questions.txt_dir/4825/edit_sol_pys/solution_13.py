

from sys import stdin, stdout

input = stdin.readline().strip()
output = ""

for i in range(len(input)):
    if input[i].isalpha():
        if input[i].isupper():
            output += chr(ord(input[i]) + 32)
        else:
            output += input[i]
    else:
        output += input[i]

output = output.replace("a", "@").replace("b", "8").replace("c", "(").replace("d", "|)").replace("e", "3").replace("f", "#").replace("g", "6").replace("h", "[-]").replace("i", "|").replace("j", "_|").replace("k", "|<").replace("l", "1").replace("m", "[]\/[]").replace("n", "[]\[]").replace("o", "0").replace("p", "|D").replace("q", "(,)").replace("r", "|Z").replace("s", "$").replace("t", "']['").replace("u", "|_|").replace("v", "\/").replace("w", "\/\/").replace("x", "}{").replace("y", "`/").replace("z", "2")

stdout.write(output)
