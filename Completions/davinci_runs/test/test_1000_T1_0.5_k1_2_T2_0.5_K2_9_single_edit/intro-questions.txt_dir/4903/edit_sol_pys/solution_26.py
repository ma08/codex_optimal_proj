
with open("test.txt", "r") as f:
    for line in f:
        jon = input()
        doc = input()
        if len(jon) >= len(doc):
            print("go")
        else:
            print("no")
