import requests
from bs4 import BeautifulSoup


def post_search(last_post, bot, channel_id):
    url = "https://timeweb.com/ru/community/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    posts = soup.find("div", class_="js-pagination-container")
    post = posts.find("article", class_="js-pagination-element cm-article-main pt-16 pb-24 mt-32:md pos-rel zi-5")
    link_post = str(post.find("a", class_="pos-abs pos-cover zi-1")).split()
    link_post = link_post[4][6:-6]

    if link_post != last_post:
        parser_data_post(link_post, bot, channel_id)
        last_post = link_post
    return last_post


def parser_data_post(link_post, bot, channel_id):
    page = requests.get(f"https://timeweb.com{link_post}")
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("article", class_="cm-article font-style-1")

    title = post.find("h1").text.strip()
    description = post.find("div", class_="cm-article__content js-article-content wb-bw").text.strip()
    text_post = f"""<b>{title}</b>\n\n{description}\n\nhttps://timeweb.com{link_post}"""

    bot.send_message(channel_id, text_post, parse_mode='html')