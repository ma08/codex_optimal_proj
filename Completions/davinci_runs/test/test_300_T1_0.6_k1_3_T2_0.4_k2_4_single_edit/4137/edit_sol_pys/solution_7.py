import os
import json

if __name__ == "__main__":
    file_list = os.listdir('./')
    for file in file_list:
        if os.path.isdir(file):
            continue
        if file.endswith('.json'):
            with open(file, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    if key == 'title':
                        print(value)
