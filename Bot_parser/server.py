import os
import telebot
import schedule
from time import sleep
from parser_data import post_search


token = os.environ["tocen"]
channel_id = os.environ["channel"]
bot = telebot.TeleBot(token)
last_post = ""


def check_posts():
    global last_post
    last_post = post_search(last_post, bot, channel_id)


schedule.every(4).seconds.do(check_posts)
if __name__ == '__main__':
    while True:
        schedule.run_pending()
        sleep(1)


bot.polling()

