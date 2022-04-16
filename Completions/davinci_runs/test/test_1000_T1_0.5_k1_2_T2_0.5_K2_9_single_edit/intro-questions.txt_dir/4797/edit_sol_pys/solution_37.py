

# Solution by Andrew Xing

def main():
  input_ = raw_input()
  output = ""
  for i in range(0, len(input_)):
    if input_[i] == "<":
      output = output[:len(output)-1]
    else:
      output += input_[i]
  print output

main()
