import requests
import json
import os

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/contents/{}".format(os.environ["USERNAME"], os.environ["REPO"], os.environ["PATH"])
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()["content"]
        print(content)
