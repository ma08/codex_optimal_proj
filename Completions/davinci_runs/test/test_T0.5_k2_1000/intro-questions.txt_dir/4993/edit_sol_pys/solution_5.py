
import sys

def main():
    """
    Main function
    """
    num_parts, num_days = map(int, input().strip().split())
    parts = set()
    for _ in range(num_days): parts.add(input().strip())
    print(num_days if len(parts) == num_parts else "paradox avoided")

if __name__ == "__main__":
    main()
