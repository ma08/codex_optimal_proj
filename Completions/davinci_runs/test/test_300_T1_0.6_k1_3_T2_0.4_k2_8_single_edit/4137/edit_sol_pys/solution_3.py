

class File:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __hash__(self):
        return hash(self.name)

if __name__ == "__main__":
    f1 = File("file1.txt")
    f2 = File("file2.txt")
    f3 = File("file3.txt")
    f4 = File("file4.txt")

    files = set()
    files.add(f1)
    files.add(f2)
    files.add(f3)
    files.add(f4)

    print(files)
