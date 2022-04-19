
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
s = input("Input a string : ")
print ("The original string  : ",end="")
print (s)
print ("The reversed string: ",end="")
print (reverse(s))
