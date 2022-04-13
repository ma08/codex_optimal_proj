

# Get the input from the user
password = input().strip()
message = input().strip()

# Set up the variables for the for loop
j = 0
i = 0

# For loop that loop until the end of the password is reached
while i < len(password)

    # If the character at index i is found in the message, it set the variable j to that index and add 1 to i
    if password[i] in message[j:]:
        j = message[j:].index(password[i]) + j + 1
        i += 1

    # If the character at index i is not found in the message, it print fail and break out of the loop
    else:
        print("FAIL")
        break

# If the loop completes, it print pass
else:
    print("PASS")
