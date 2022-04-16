#
#  File:
#    file.py
#
#  Synopsis:
#    Illustrates how to read and write a file.
#
#  Categories:
#    file input/output
#
#  Author:
#    Fred Clare (based on an original example by Karin Meier-Fleischer)
#  
#  Date of initial publication:
#    November, 2005
#
#  Description:
#    This example shows how to read and write a file.
#
#  Effects illustrated:
#    o  Reading a file.
#    o  Writing a file.
# 
#  Output:
#    This example produces two files, one containing the original
#    data and one containing the modified data.
#
#  Notes:
#     

import Ngl


def main():

#--  Open the input file.
  r = open("file.in","r")

#--  Read the input file and store the data in a list.
  in_data = []
  for line in r.readlines():
    in_data.append(line.split())

#--  Close the input file.
  r.close()

#--  Print the original data.
  print("Original data:")
  for i in range(len(in_data)):
    print(in_data[i])

#--  Modify the data.
  out_data = []
  for i in range(len(in_data)):
    out_data.append(in_data[i]*2)

#--  Print the modified data.
  print("Modified data:")
  for i in range(len(out_data)):
    print(out_data[i])

#--  Open the output file.
  w = open("file.out","w")

#--  Write the modified data to the output file.
  for i in range(len(out_data)):
    for j in range(len(out_data[i])):
      w.write(str(out_data[i][j])+" ")
    w.write("\n")

#--  Close the output file.
  w.close()

main()
