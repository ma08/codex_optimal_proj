# def main():
#     # Get inputs
#     n, V = map(int, input().split())
#     boxes = []
#     for i in range(n):
#         boxes.append(tuple(map(int, input().split())))
#     # Calculate volumes of each box
#     volumes = []
#     for box in boxes:
#         volumes.append(box[0] * box[1] * box[2])
#     # Find largest box
#     largest = max(volumes)
#     # Calculate difference
#     difference = largest - V
#     # Print difference
#     print(difference)


# if __name__ == '__main__':
#     main()

import sys

def main(argv):
    print(argv)

if __name__ == "__main__":
   main(sys.argv[1:])
