

def is_harshad(n):
  return n % sum(map(int, str(n))) == 0

def main():
  n = int(input())
  print("Yes" if is_harshad(n) else "No")

if __name__ == "__main__":
  main()