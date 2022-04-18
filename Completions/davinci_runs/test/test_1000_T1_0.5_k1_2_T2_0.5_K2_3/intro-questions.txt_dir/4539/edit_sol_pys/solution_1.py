

def is_harashad(num):
  return num % sum(map(int, str(num))) == 0

def main():
  num = int(input())
  print("Yes" if is_harashad(num) else "No")

if __name__ == "__main__":
  main()
