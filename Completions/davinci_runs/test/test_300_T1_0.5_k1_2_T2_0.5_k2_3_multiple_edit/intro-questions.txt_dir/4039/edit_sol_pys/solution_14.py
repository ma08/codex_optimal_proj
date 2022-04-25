
import json



def fix_spelling(dictionary, misspelled_word):
    with open('dictionary.json') as f:
        data = json.load(f)
    if misspelled_word in data:
        return data[misspelled_word]
    else:
        return None


def main():
    pass


if __name__ == "__main__":
    main()
