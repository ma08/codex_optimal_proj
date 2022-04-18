"""
Problem
You’ve just finished writing a piece of code that calculates the amount of memory
that will be used to store a given string. You know the following:
• Each character of the string requires 1 byte of memory.
• Each integer or floating-point value requires 4 bytes of memory.
• Each Boolean value requires 1 byte of memory.
• Each reference to an object requires 4 bytes of memory.
• The String class stores the length of the string in an integer value.
• The String class stores the internal character array using a reference to an object.
• The String class stores the hashcode of the string in an integer value.
• The String class stores the reference to the string’s comparator in an object reference.
• The String class stores the cached string representation in a reference to an object.
• The String class stores the reference to the string’s case mapping table in an object reference.
• The String class stores a reference to the string’s cached string representation in an object reference.
• The String class stores a reference to the string’s cached hashcode in an integer value.
• The String class stores a reference to the string’s cached comparator in an object reference.
• The String class stores a reference to the string’s cached case mapping table in an object reference.
Write a program that asks the user to input the number of characters in a string and
then prints the amount of memory that would be required to store the string.
"""

"""
Solution 
"""

def main():
    X = int(input())
    N = int(input())
    megabytes = X
    for i in range(N):
        megabytes = megabytes - int(input())
    print(megabytes)

if __name__ == '__main__':
    main()
