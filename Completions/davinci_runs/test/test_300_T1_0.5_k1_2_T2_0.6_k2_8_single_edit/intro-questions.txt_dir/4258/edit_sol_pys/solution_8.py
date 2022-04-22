from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import time


# url = 'https://www.google.com/search?q=hello&rlz=1C1GCEA_enUS788US788&oq=hello&aqs=chrome..69i57j0l5.4270j0j4&sourceid=chrome&ie=UTF-8'
# word = input("Enter a word: ")
#
# url = 'https://www.google.com/search?q=' + word + '&rlz=1C1GCEA_enUS788US788&oq=' + word + '&aqs=chrome..69i57j0l5.4270j0j4&sourceid=chrome&ie=UTF-8'
#
# print(url)



# url = 'https://www.google.com/search?q=hello&rlz=1C1GCEA_enUS788US788&oq=hello&aqs=chrome..69i57j0l5.4270j0j4&sourceid=chrome&ie=UTF-8'



def main():
    word = input("Enter a word: ")

    url = 'https://www.google.com/search?q=' + word + '&rlz=1C1GCEA_enUS788US788&oq=' + word + '&aqs=chrome..69i57j0l5.4270j0j4&sourceid=chrome&ie=UTF-8'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")


    with open('test.txt', 'w') as file:
        for link in soup.find_all('a'):
            print(link.get('href'))
            file.write(str(link.get('href')))
            file.write('\n')

    time.sleep(10)




if __name__ == '__main__':
    main()



