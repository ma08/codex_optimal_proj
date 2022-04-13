

# Solution by Andrew Xing, edited by Gerald

def main():
  input = input()
  output = ""
  for i in range(0, len(input)):
    if input[i] == "<":
      output = output[:len(output)-1]
    else:
      output += input[i]
  print(output)

if __name__ == "__main__":
  main()
