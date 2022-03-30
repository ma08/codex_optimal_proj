import json
import os
import pathlib

def create_split(split="train", name="train"):
    paths = []
    roots = sorted(os.listdir(split))
    for folder in roots:
        root_path = os.path.join(split, folder)
        paths.append(root_path)


    with open(name+".json", "w") as f:
        json.dump(paths, f)
    
    return paths

#Choose the target train-test pair (since we are only testing, those can actually be used both as testing sets)
training_sort_problems="../APPS_subdataset/train/sort-questions.txt_dir/"
testing_sort_problems="../APPS_subdataset/test/sort-questions.txt_dir/"
training_search_problems="../APPS_subdataset/train/search-questions.txt_dir/"
testing_sort_problems="../APPS_subdataset/test/search-questions.txt_dir/"

paths_to_probs = [training_sort_problems, testing_sort_problems]
names = ["train", "test"]

all_paths = []
for index in range(len(paths_to_probs)):
    all_paths.extend(create_split(split=paths_to_probs[index], name=names[index]))

with open("train_and_test.json", "w") as f:
    print(f"Writing all paths. Length = {len(all_paths)}")
    json.dump(all_paths, f)
