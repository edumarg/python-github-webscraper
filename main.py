import requests
from bs4 import BeautifulSoup as bs


def get_user_info():
    response = requests.get(url=url)
    soup = bs(response.content, 'html.parser')
    return soup


def get_user_image():
    user_info = get_user_info()
    user_image = user_info.find('img', {'alt': 'Avatar'})['src']
    print('user image: ', user_image)


def get_user_name():
    user_info = get_user_info()
    user_name = user_info.find('span', {'itemprop': 'name'}).getText().strip()
    if user_name:
        print('user name: ', user_name)
    else:
        print('user name: ', "N/A")


def get_uer_web_page():
    user_info = get_user_info()
    try:
        user_web_page = user_info.find('a', {'rel': 'nofollow me'})['href']
        if (user_web_page):
            print('user webpage: ', user_web_page)
        else:
            print('user webpage: ', "N/A")
    except TypeError:
        print('user webpage: ', "N/A")


if __name__ == '__main__':
    github_user = input("Please input GitHub user name: ")
    url = f'https://github.com/{github_user}'
    get_user_image()
    get_user_name()
    get_uer_web_page()
