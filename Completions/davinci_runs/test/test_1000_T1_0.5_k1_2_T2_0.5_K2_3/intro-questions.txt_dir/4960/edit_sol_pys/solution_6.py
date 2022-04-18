#!/usr/bin/env python3

#-----main-----
def main():
	binNum = input()
	num = len(binNum)
	if num % 3 == 1:
		binNum = "00" + binNum
	elif num % 3 == 2:
		binNum = "0" + binNum
	octNum = ""
	for i in range(0, num, 3):
		octNum += str(int(binNum[i : i+3], 2))
	print(octNum)

main()
