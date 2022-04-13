
import sys

def main():
    message = sys.stdin.readline().rstrip()
    half = int(len(message)/2)
    rotate1 = rotate2 = 0
    for i in range(half):
        rotate1 += ord(message[i]) - 65
        rotate2 += ord(message[half+i]) - 65
    rotate1 %= 26
    rotate2 %= 26
    for i in range(half):
        message = message[:i] + chr((ord(message[i]) - 65 + rotate1) % 26 + 65) + message[i+1:]
        message = message[:half+i] + chr((ord(message[half+i]) - 65 + rotate2) % 26 + 65) + message[half+i+1:]
    for i in range(half):
        message = message[:i] + chr((ord(message[i]) - 65 + ord(message[half+i]) - 65) % 26 + 65) + message[i+1:]
    print(message[:half])

main()
