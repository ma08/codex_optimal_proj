

def main():
    message = input()
    half1 = message[:len(message)//2]
    half2 = message[len(message)//2:]
    
    sum1 = 0
    sum2 = 0
    for i in range(len(half1)):
        sum1 += ord(half1[i]) - ord('a')
        sum2 += ord(half2[i]) - ord('a')
    sum1 = sum1 % 26
    sum2 = sum2 % 26
    
    new1 = ""
    new2 = ""
    for i in range(len(half1)):
        new1 += chr(((ord(half1[i]) - ord('a') + sum1) % 26) + ord('a'))
        new2 += chr(((ord(half2[i]) - ord('a') + sum2) % 26) + ord('a'))
    
    final = ""
    for i in range(len(new1)):
        final += chr(((ord(new1[i]) - ord('a') + ord(new2[i]) - ord('a')) % 26) + ord('a'))
    
    print(final)

if __name__ == "__main__":
    main()
