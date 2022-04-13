
import sys

def main():
    message = sys.stdin.readline().strip()
    half = int(len(message)/2)
    rotate1 = rotate2 = 0
    for i in range(half):
        rotate1 += ord(message[i]) - ord('A')
        rotate2 += ord(message[half+i]) - ord('A')
    rotate1 %= 26
    rotate2 %= 26
    for i in range(half):
        message = message[:i] + chr((ord(message[i]) - ord('A') + rotate1) % 26 + ord('A')) + message[i+1:]
        message = message[:half+i] + chr((ord(message[half+i]) - ord('A') + rotate2) % 26 + ord('A')) + message[half+i+1:]
    for i in range(half):
        message = message[:i] + chr((ord(message[i]) - ord('A') + ord(message[half+i]) - ord('A')) % 26 + ord('A')) + message[i+1:]
    print(message[:half])

main()
