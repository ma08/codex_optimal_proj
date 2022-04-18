import requests
import json
import time
import os


def get_file_list():
    """
    Get the list of files in the directory.
    """
    file_list = []
    for file in os.listdir("./"):
        if file.endswith(".txt"):
            file_list.append(file)
    return file_list


def get_data(filename):
    """
    Get the data from the file.
    """
    with open(filename, "r") as file:
        data = file.readlines()
    return data


def get_json(data):
    """
    Get the json data from the api.
    """
    url = "https://api.github.com/graphql"
    headers = {"Authorization": "bearer " + data[0].strip()}
    payload = {"query": data[1].strip()}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, response.text))


def get_repository_data(json):
    """
    Get the repository data from the json.
    """
    repository_data = json["data"]["search"]["nodes"]
    return repository_data


def get_repository_list(repository_data):
    """
    Get the list of repositories.
    """
    repository_list = []
    for repository in repository_data:
        repository_list.append(repository["nameWithOwner"])
    return repository_list


def write_repository_list(repository_list, filename):
    """
    Write the list of repositories to the file.
    """
    with open(filename, "w") as file:
        for repository in repository_list:
            file.write(repository + "\n")


def get_repository_count(repository_data):
    """
    Get the count of repositories.
    """
    return len(repository_data)


def write_repository_count(repository_count, filename):
    """
    Write the repository count to the file.
    """
    with open(filename, "w") as file:
        file.write("{}".format(repository_count))


def run():
    """
    Run the program.
    """
    file_list = get_file_list()
    for file in file_list:
        data = get_data(file)
        json = get_json(data)
        repository_data = get_repository_data(json)
        repository_list = get_repository_list(repository_data)
        write_repository_list(repository_list, "repository_list.txt")
        repository_count = get_repository_count(repository_data)
        write_repository_count(repository_count, "repository_count.txt")
        print(file, "done.")
        time.sleep(1)
