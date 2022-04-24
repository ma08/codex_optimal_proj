

# from itertools import combinations

# n = int(input())
# l = sorted(list(map(int, input().split())))

# count = 0
# for i in combinations(l, 3):
#     if i[0] + i[1] > i[2]:
#         count += 1



# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:i + len(sub_string)] == sub_string:
#             count += 1
#     return count


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)


# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:i + len(sub_string)] == sub_string:
#             count += 1
#     return count


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)


# def string_validators(s):
#     print(any(char.isalnum() for char in s))
#     print(any(char.isalpha() for char in s))
#     print(any(char.isdigit() for char in s))
#     print(any(char.islower() for char in s))
#     print(any(char.isupper() for char in s))


# if __name__ == '__main__':
#     s = input()
#     string_validators(s)


# def minion_game(string):
#     vowels = "AEIOU"
#     kevin = 0
#     stuart = 0
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin += len(string) - i
#         else:
#             stuart += len(string) - i

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif kevin < stuart:
#         print("Stuart", stuart)
#     else:
#         print("Draw")


# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# def minion_game(string):
#     vowels = "AEIOU"
#     kevin = 0
#     stuart = 0
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin += len(string) - i
#         else:
#             stuart += len(string) - i

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif kevin < stuart:
#         print("Stuart", stuart)
#     else:
#         print("Draw")


# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# def minion_game(string):
#     vowels = "AEIOU"
#     kevin = 0
#     stuart = 0
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin += len(string) - i
#         else:
#             stuart += len(string) - i

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif kevin < stuart:
#         print("Stuart", stuart)
#     else:
#         print("Draw")


# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# def minion_game(string):
#     vowels = "AEIOU"
#     kevin = 0
#     stuart = 0
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin += len(string) - i
#         else:
#             stuart += len(string) - i

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif kevin < stuart:
#         print("Stuart", stuart)
#     else:
#         print("Draw")


# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# def minion_game(string):
#     vowels = "AEIOU"
#     kevin = 0
#     stuart = 0
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin += len(string) - i
#         else:
#             stuart += len(string) - i

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif kevin < stuart:
#         print("Stuart", stuart)
#     else:
#         print("Draw")


# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# def minion_game(string):
#     vowels = "AEIOU"
#     kevin = 0
#     stuart = 0
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin += len(string) - i
#         else:
#             stuart += len(string) - i

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif kevin < stuart:
#         print("Stuart", stuart)
#     else:
#         print("Draw")


# if __name__ == '__main__':
#     s = input()
#     minion_game(s)
# print(count)
