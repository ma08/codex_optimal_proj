

# import numpy as np
# import pandas as pd

# df = pd.read_csv("test.csv")

# df["x"] = np.zeros(len(df))
# df["y"] = np.zeros(len(df))

# df.to_csv("test.csv", index=False)

import csv

with open("test.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# with open("test.csv", "r") as f:
#     reader = csv.reader(f)
#     l = [row for row in reader]
#     print(l)
