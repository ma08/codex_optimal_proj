

def is_valid(proof):
    """
    Given a list of lines of a "proof", determine whether it is valid.
    """
    # The set of all previous assumptions
    prev_assumptions = set()
    # The set of all current conclusions
    curr_conclusions = set()

    for line in proof:
        # Split the line into conclusion and assumptions
        split = line.split(" -> ")
        conclusion = split[0]
        assumptions = split[1]

        # If there are no assumptions, the conclusion is an axiom, so just add it to the set of current conclusions
        if assumptions == "":
            curr_conclusions.add(conclusion)
        else:
            # Otherwise, each assumption must be in the set of previous assumptions
            for assumption in assumptions.split():
                if assumption not in prev_assumptions:
                    return False
            curr_conclusions.add(conclusion)

        # Add the current conclusions to the set of previous assumptions
        prev_assumptions.update(curr_conclusions)

    return True


def main():
    # Read the number of lines in the proof
    n = int(input())
    # Read the proof
    proof = [input() for _ in range(n)]

    # Determine whether the proof is valid
    valid = is_valid(proof)

    if valid:
        print("correct")
    else:
        # If the proof is not valid, print the line number of the first invalid line
        for i, line in enumerate(proof):
            split = line.split(" -> ")
            conclusion = split[0]
            assumptions = split[1]

            if assumptions == "":
                if conclusion not in curr_conclusions:
                    print(i+1)
                    break
            else:
                for assumption in assumptions.split():
                    if assumption not in curr_conclusions:
                        print(i+1)
                        break
                else:
                    continue
                break


if __name__ == "__main__":
    main()
