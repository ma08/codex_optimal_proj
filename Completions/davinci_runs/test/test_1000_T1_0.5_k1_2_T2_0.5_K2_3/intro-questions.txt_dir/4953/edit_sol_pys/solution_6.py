
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
    # Find all characters who speak a unique language
    unique_languages = [char.speaks for char in characters]
    unique_languages = list(set(unique_languages))
    unique_languages_counts = [unique_languages.count(char.speaks) for char in characters]
    unique_languages_counts = list(set(unique_languages_counts))
    # If a character speaks a unique language, then they must leave
    if 1 in unique_languages_counts:
        return unique_languages_counts.count(1)
    # Otherwise, we have to find the largest set of characters who can converse
    # with each other
    else:
        return max([len(set(characters) - set(char.can_converse(characters))) for char in characters])

class Character:
    """
    Character class.
    """
    def __init__(self, input_line):
        """
        Initializes a character.
        """
        self.name, self.speaks, *self.understands = input_line.split()

    def can_converse(self, characters):
        """
        Returns a list of all characters that the character can converse with.
        """
        can_converse = []
        # For each character in the list of characters
        for char in characters:
            # If the character can converse with the character, then add them
            # to the list of characters that can converse with the character
            if char.can_converse_with(self):
                can_converse.append(char)
        return can_converse

    def can_converse_with(self, character):
        """
        Returns True if the character can converse with the given character,
        otherwise returns False.
        """
        # If the character speaks the same language as the given character,
        # then they can converse
        if self.speaks == character.speaks:
            return True
        # If the character understands the language that the given character
        # speaks, then they can converse
        elif self.speaks in character.understands:
            return True
        # If the given character understands the language that the character
        # speaks, then they can converse
        elif character.speaks in self.understands:
            return True
        # Otherwise, the characters cannot converse
        else:
            return False

if __name__ == "__main__":
    main()
