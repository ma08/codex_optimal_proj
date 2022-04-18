

def is_valid(proof):
    """
    Given a list of lines of a "proof", determine whether it is valid.
    """
    # The set of all previous conclusions
    prev_conclusions = set()
    # The set of all current assumptions
    curr_assumptions = set()

    for i, line in enumerate(proof):
        # Split the line into assumptions and conclusion
        split = line.split(" -> ")
        assumptions = split[0]
        conclusion = split[1]

        # If there are no assumptions, the conclusion is an axiom
        if assumptions == "":
            curr_assumptions.add(conclusion)
        else:
            # Otherwise, each assumption must be in the set of previous conclusions
            for assumption in assumptions.split():
                if assumption not in prev_conclusions:
                    return i+1
            curr_assumptions.add(conclusion)

        # Add the current assumptions to the set of previous conclusions
        prev_conclusions.update(curr_assumptions)

    return True


def main():
    # Read the number of lines in the proof
    n = int(input())
    # Read the proof
    proof = [input() for _ in range(n)]

    # Determine the first invalid line
    line_number = is_valid(proof)

    if line_number == -1:
        print("correct")
    else:
        # If the proof is not valid, print the line number of the first invalid line
        print(line_number)


if __name__ == "__main__":
    main()
