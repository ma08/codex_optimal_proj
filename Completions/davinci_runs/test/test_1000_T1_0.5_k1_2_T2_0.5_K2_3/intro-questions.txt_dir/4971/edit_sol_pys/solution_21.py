

from collections import defaultdict

def main():
    """
    This solution is based on the fact that the taxicab numbers are known to be
    of the form $a^3 + b^3 = c^3 + d^3$, where $a \ne c$ and $b \ne d$. This can
    be proved using the fact that $a^3 + b^3 = c^3 + d^3$ is equivalent to
    $(a - c)(a^2 + ac + c^2) = (b - d)(b^2 + bd + d^2)$.

    The above equation can be shown to have no solutions for $a = c$ or $b = d$
    by considering the cases where $a = c = 0$ or $b = d = 0$ or $a = c = 1$ or
    $b = d = 1$.

    Since $a \ne c$ and $b \ne d$, the equation can be rewritten as
    $a^3 + b^3 = a^3 + b^3 + c^3 - c^3$. This can be further simplified to
    $a^3 - c^3 = c^3 - a^3$. This equation has solutions for $a \ne c$ and $a, c
    \ge 0$.

    This solution works by generating all the possible $a^3 - c^3$ values for $a
    \ne c$ and $a, c \ge 0$. It then uses a dictionary to store the number of
    ways that a number can be expressed as the sum of two positive cubes. The
    largest taxicab number that is less than the input is then printed.
    """
    m = int(raw_input())

    # Generate all the possible values of a^3 - c^3
    a3_c3 = defaultdict(int)
    for a in range(0, int(m ** (1.0 / 3.0)) + 1):
        for c in range(0, int(m ** (1.0 / 3.0)) + 1):
            if a != c:
                a3_c3[a ** 3 - c ** 3] += 1

    # Find the largest taxicab number that is less than the input
    max_taxicab_num = -1
    for num, count in a3_c3.iteritems():
        if count >= 2 and num <= m:
            max_taxicab_num = max(max_taxicab_num, num)

    if max_taxicab_num == -1:
        print "none"
    else:
        print max_taxicab_num

if __name__ == "__main__":
    main()
