
import sys

def main():
    """
    Main Function
    """
    num_parts, num_days = sys.stdin.readline().strip().split()
    num_parts = int(num_parts)
    num_days = int(num_days)
    parts = {}
    for _ in range(num_days):
        part = sys.stdin.readline().strip()
        if part in parts:
            parts[part] += 1
        else:
            parts[part] = 1
    if len(parts) == num_parts:
        print(num_days)
    else:
        print("paradox avoided")

if __name__ == "__main__":
    main()
