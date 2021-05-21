import re
from pathlib import Path
from datetime import datetime
from selenium import webdriver

SITE = 'www.y8.com'
PATH = f'site/{SITE}'
URL = f'https://{SITE}/'

browser = webdriver.Firefox()

Path('site').mkdir(exist_ok=True)
Path(PATH).mkdir(exist_ok=True)

browser.get(URL)
browser.find_element_by_tag_name('body') \
        .screenshot(f'{PATH}/{SITE} {datetime.now().strftime("%d.%m.%Y")}.png')

urls = []
for thumb in browser.find_elements_by_class_name('item'):
    urls.append(thumb.find_element_by_tag_name('a').get_attribute('href'))

for game_url in urls:
    print(f'Fetching {game_url}')
    browser.get(game_url)
    game_name = browser.find_element_by_class_name('game-info-container').find_element_by_tag_name('h1').text
    file_name = re.sub("[^\w\s-]", "", game_name).strip()
    game_description = '\n\n'.join(
        [x.text for x in browser.find_element_by_class_name('game-description').find_elements_by_tag_name('p')]
    )
    browser.find_element_by_tag_name('body') \
        .screenshot(f'{PATH}/{file_name} {datetime.now().strftime("%d.%m.%Y")}.png')
    with open(f'{PATH}/{file_name} {datetime.now().strftime("%d.%m.%Y")}.txt', 'w') as fp:
        fp.write(game_description)

browser.close()

