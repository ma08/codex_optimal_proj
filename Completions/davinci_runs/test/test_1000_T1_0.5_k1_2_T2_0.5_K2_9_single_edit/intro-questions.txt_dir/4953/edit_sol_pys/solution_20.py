

def main():
    """
    Main function.
    """
    num_characters = int(input())
    characters = []
    for i in range(num_characters):
        characters.append(Character(input()))
    print(solve(characters))

def solve(characters):
    """
    Solves the problem.
    """
    pass

class Character:
    """
    Character class.
    """
        pass

if __name__ == "__main__":
    main()
