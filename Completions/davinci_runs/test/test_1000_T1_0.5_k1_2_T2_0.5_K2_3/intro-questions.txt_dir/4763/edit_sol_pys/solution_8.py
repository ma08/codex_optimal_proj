
def main():
    target_score = int(input())

    # Check if the target score is impossible
    if target_score > 180:
        print("impossible")
        return

    # Loop through the scores of single, double, and triple
    while target_score > 0:
        # Find the highest single score possible
        if target_score >= 20:
            single = 20
        else:
            single = target_score

        # Find the highest double score possible
        if target_score >= 40:
            double = 40
        else:
            double = target_score // 2

        # Find the highest triple score possible
        if target_score >= 60:
            triple = 60
        else:
            triple = target_score // 3

        # Print the highest score
        if single >= double and single >= triple:
            print("single", single)
            target_score -= single
        elif double >= single and double >= triple:
            print("double", double)
            target_score -= double * 2
        else:
            print("triple", triple)
            target_score -= triple * 3

main()
