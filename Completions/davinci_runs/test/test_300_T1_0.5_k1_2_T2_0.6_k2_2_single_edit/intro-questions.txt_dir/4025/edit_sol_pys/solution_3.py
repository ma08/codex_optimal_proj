
import re

def main():
    string = "1 2 3"
    # string = "3 2 1"
    nums = re.findall(r'\d+', string)
    nums = [int(i) for i in nums]
    print(nums)

if __name__ == "__main__":
    main()
