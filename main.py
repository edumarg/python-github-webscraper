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


def get_user_bio():
    user_info = get_user_info()
    user_bio = user_info.find('div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'}).getText().strip()
    if user_bio:
        print('user bio: ', user_bio)
    else:
        print('user bio: ', 'N/A')


def get_repositories(user):
    user_info = get_user_info()
    user_repositories = user_info.find('a', {'href': f'/{user}?tab=repositories'})
    user_number_of_repositories = user_repositories.find('span', {'class': 'Counter'}).getText().strip()
    print('user repositories: ',
          f'{user} has {user_number_of_repositories} repositories located at https://github.com/{user_repositories["href"]}')


def get_uer_web_page():
    user_info = get_user_info()
    try:
        user_web_page = user_info.find('a', {'rel': 'nofollow me'})['href']
        if user_web_page:
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
    get_user_bio()
    get_repositories(github_user)
    get_uer_web_page()
