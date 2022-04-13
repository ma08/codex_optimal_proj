
#
# import sys
#
# def main():
#     passwords = [] # list of passwords and their probabilities
#     for line in sys.stdin:
#         passwords.append(line.strip().split()) # split line into password and probability
#     passwords = [[int(p), float(prob)] for p, prob in passwords] # convert to int and float
#     passwords.sort(key=lambda x: x[1], reverse=True) # sort in descending order of probabilities
#     # print(passwords)
#     expected = 0
#     for i in range(len(passwords)):
#         expected += (i + 1) * passwords[i][1]
#     print(expected)
#
# if __name__ == "__main__":
#     main()
