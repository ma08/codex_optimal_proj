class File:
    def __init__(self, name, size, owner, group, permissions):
        self.name = name
        self.size = size
        self.owner = owner
        self.group = group
        self.permissions = permissions

if __name__ == "__main__":
    file = File("file.txt", 10, "root", "root", "rwx")
    print(file.name)
    print(file.size)
    print(file.owner)
    print(file.group)
    print(file.permissions)
