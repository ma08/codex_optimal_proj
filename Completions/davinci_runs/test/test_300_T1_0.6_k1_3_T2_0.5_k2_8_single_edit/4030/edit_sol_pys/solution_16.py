


import sys

class Solver:
    def __init__(self, n, s):
        self.n = n

        self.s = s
        """
        Returns colors of the input string
        """


    def solve(self):
        def get_colors(s):
            colors = [1]
            for i in range(1, len(s)):
                if s[i] != s[i - 1]:

                    colors.append(colors[i - 1] + 1)
                else:
                    colors.append(colors[i - 1])
            return colors

        # colors of the input string
        colors = get_colors(self.s)
        # colors of the sorted input string
        sorted_colors = get_colors(sorted(self.s))
        return [max(colors), " ".join(map(str, colors))]


if __name__ == "__main__":
    n = int(input())
    s = input()

    solver = Solver(n, s)
    res = solver.solve()
    print(res[0])
    print(res[1])
