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
browser.quit()