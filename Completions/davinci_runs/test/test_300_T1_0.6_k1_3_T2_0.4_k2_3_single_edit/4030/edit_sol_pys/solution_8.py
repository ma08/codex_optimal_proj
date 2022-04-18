class Solver:
    def __init__(self, n, s_):
        self.n = n  # type: int
        self.s = s_  # type: str

    def solve(self):
        def get_colors(s_):
            # type: (str) -> list[int]
            colors = [1]
            for i in range(1, len(s)):
                if s[i] != s[i - 1]:
                    colors.append(colors[i - 1] + 1)
                else:
                    colors.append(colors[i - 1])
            return colors

        colors = get_colors(self.s)
        sorted_colors = get_colors(sorted(self.s))
        return [max(colors), " ".join(map(str, colors))]


if __name__ == "__main__":
    n = int(input())
    s = input()

    solver = Solver(n, s)
    res = solver.solve()
    print(res[0])
    print(res[1])
