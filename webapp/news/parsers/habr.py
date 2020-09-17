from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import get_html, save_news

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'russian')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU')


def get_habr_snippets():
    html = get_html('https://habr.com/ru/search/?target_type=posts&q=python&order_by=date')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='content-list_posts').findAll('li', class_="content-list__item_post")
        for news in all_news:
            title = news.find('a', class_='post__title_link').text
            url = news.find('a', class_='post__title_link')["href"]
            published = news.find('span', class_='post__time').text
            print(title, url, published)
            """
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except (ValueError):
                published = datetime.now()
            save_news(title, url, published)
            """