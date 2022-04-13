

def main():
    n = int(input())
    languages = list(map(int, input().split()))

    # All guests are speaking different languages, so the awkwardness level is n
    if len(set(languages)) == n:
        print(n)
        return

    # Sort the languages, and find the position of the first language in the sorted list
    languages_sorted = sorted(languages)
    first_language = languages_sorted[0]

    # Find the positions of the first and last occurrences of the first language
    first_language_positions = [i for i, x in enumerate(languages) if x == first_language]
    first_language_first_position = first_language_positions[0]
    first_language_last_position = first_language_positions[-1]

    # Find the positions of the first and last occurrences of the second language
    second_language = languages_sorted[1]
    second_language_positions = [i for i, x in enumerate(languages) if x == second_language]
    second_language_first_position = second_language_positions[0]
    second_language_last_position = second_language_positions[-1]

    # Find the awkwardness level
    if first_language_first_position < second_language_first_position:
        # The first and second language are not adjacent
        awkwardness_level = min(first_language_last_position - second_language_first_position, second_language_last_position - first_language_first_position) - 1
    else:
        # The first and second language are adjacent
        awkwardness_level = min(first_language_last_position - second_language_first_position, second_language_last_position - first_language_first_position) - 1 + 1

    print(awkwardness_level)

if __name__ == '__main__':
    main()
