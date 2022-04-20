
# Heron's formula
def area(a,b,c):
  s = (a+b+c)/2
  return (s*(s-a)*(s-b)*(s-c))**(1/2)


if __name__ == '__main__':
  a,b,c = map(int,input().split())
  print(int(area(a,b,c)))
