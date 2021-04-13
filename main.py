import requests
from bs4 import BeautifulSoup as bs


def get_user_info():
    response = requests.get(url=url)
    soup = bs(response.content, 'html.parser')
    return soup


if __name__ == '__main__':
    github_user = input("Please input GitHub user name: ")
    url = f'https://github.com/{github_user}'
