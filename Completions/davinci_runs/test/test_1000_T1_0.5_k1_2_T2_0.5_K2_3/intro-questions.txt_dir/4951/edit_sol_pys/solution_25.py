

def is_correct(proof):
    """
    Given a list of lines of a "proof", determine whether it is correct.
    """
    # The set of all previous conclusions
    prev_conclusions = set()
    # The set of all current assumptions
    curr_assumptions = set()

    for line in proof:
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
                    return False
            curr_assumptions.add(conclusion)

        # Add the current assumptions to the set of previous conclusions
        prev_conclusions.update(curr_assumptions)

    return True


def main():
    # Read the number of lines in the proof
    n = int(input())
    # Read the proof
    proof = [input() for _ in range(n)]

    # The set of all previous conclusions
    prev_conclusions = set()
    # The set of all current assumptions
    curr_assumptions = set()

    # Determine whether the proof is correct
    correct = is_correct(proof)

    if correct:
        print("correct")
    else:
        # If the proof is not correct, print the line number of the first incorrect line
        for i, line in enumerate(proof):
            split = line.split(" -> ")
            assumptions = split[0]
            conclusion = split[1]

            if assumptions == "":
                if conclusion not in prev_conclusions:
                    print(i+1)
                    break
            else:
                for assumption in assumptions.split():
                    if assumption not in prev_conclusions:
                        print(i+1)
                        break
                else:
                    continue
                break


if __name__ == "__main__":
    main()
