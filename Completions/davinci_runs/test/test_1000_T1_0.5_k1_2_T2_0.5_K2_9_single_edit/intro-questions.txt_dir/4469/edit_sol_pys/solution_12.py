


def get_characters():
    # Get the number of characters
    n = int(input())

    # Get the characters
    characters = input().split()

    return n, characters


def get_queries():
    # Get the number of queries
    q = int(input())

    # Get the queries
    queries = []
    for i in range(q):
        queries.append(input())

    return q, queries


def get_substrings(string, length):
    # Initialize the list of substrings
    substrings = []

    # Loop over the characters
    for i in range(len(string) - length + 1):
        # Add the substring to the list
        substrings.append(string[i:i + length])

    return substrings


def get_substring_counts(substrings):
    # Initialize the counts
    counts = {}

    # Loop over the substrings
    for substring in substrings:
        # If the substring is already in the counts
        if substring in counts:
            # Increment the count
            counts[substring] += 1

        # If the substring is not in the counts
        else:
            # Set the count to 1
            counts[substring] = 1

    return counts


def get_substring_probabilities(substring_counts, n, length):
    # Initialize the probabilities
    probabilities = {}

    # Loop over the substrings
    for substring in substring_counts:
        # Get the probability
        probabilities[substring] = substring_counts[substring] / (n - length + 1)

    return probabilities


def get_best_probabilities(probabilities):
    # Initialize the return value
    best_probabilities = []

    # Initialize the best probability
    best_probability = 0

    # Loop over the substrings
    for substring in probabilities:
        # If the probability is greater than the best probability
        if probabilities[substring] > best_probability:
            # Set the best probability
            best_probability = probabilities[substring]

    # Loop over the substrings
    for substring in probabilities:
        # If the probability is equal to the best probability
        if probabilities[substring] == best_probability:
            # Add the substring to the list
            best_probabilities.append(substring)

    return best_probabilities


def print_best_probabilities(best_probabilities):
    # Sort the substrings
    best_probabilities.sort()

    # Loop over the substrings
    for substring in best_probabilities:
        # Print the substring
        print(substring)



def main():
    # Get the characters
    n, characters = get_characters()

    # Get the queries
    q, queries = get_queries()

    # Loop over the lengths
    for i in range(q):
        # Get the length
        length = int(queries[i])

        # Get the substrings
        substrings = get_substrings(characters, length)

        # Get the substring counts
        substring_counts = get_substring_counts(substrings)

        # Get the substring probabilities
        substring_probabilities = get_substring_probabilities(substring_counts, n, length)

        # Get the best probabilities
        best_probabilities = get_best_probabilities(substring_probabilities)

        # Print the best probabilities
        print_best_probabilities(best_probabilities)


if __name__ == "__main__":
    main()
