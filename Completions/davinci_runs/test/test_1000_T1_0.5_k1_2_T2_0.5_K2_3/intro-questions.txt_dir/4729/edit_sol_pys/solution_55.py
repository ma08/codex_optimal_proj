

# # Gets the input from the user
# password = input().strip()
# message = input().strip()

# # Sets up the variables for the for loop
# j = 0
# i = 0

# # For loop that loops until the end of the password is reached
# while i < len(password):

#     # If the character at index i is found in the message, it sets the variable j to that index and adds 1 to i.
#     if password[i] in message[j:]:
#         j = message[j:].index(password[i]) + j + 1
#         i += 1

#     # If the character at index i is not found in the message, it prints fail and breaks out of the loop
#     else:
#         print("FAIL")
#         break

# # If the loop completes, it prints pass
# else:
#     print("PASS")
#

def is_substring(string, sub):
    if string.find(sub) == -1:
        return False
    else:
        return True


def is_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)


print(is_rotation("water", "aterw"))
