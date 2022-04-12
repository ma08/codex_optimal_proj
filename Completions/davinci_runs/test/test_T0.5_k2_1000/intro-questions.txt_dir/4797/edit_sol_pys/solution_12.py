

# Solution by Andrew Xing 

def main():
  input = input()
  output = ""
  for i in range(0, len(input)):
    if input[i] == "<":
      output = output[:len(output)-1]
    else:
      output += input[i]
  print output

main()
