

class File:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

    def rename(self, newName):
        self.name = newName
