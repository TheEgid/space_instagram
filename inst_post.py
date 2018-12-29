"""Instagram publication module."""
import os
import sys
import time
import random
import logging
from instabot import Bot

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.split(dir_path)[0])
logging.basicConfig(level=logging.INFO)


def inst_publish(login, password, folder_name, extension, timeout_value=10):
    """Instagram image posting from folder.

    Args:
        login(str): instagram login
        password(str): instagram password
        folder_name(str): image file folder
        extension(str): image file extension
        timeout_value(int): randomized timeout of posting

    """
    posted_pic_list = []
    try:
        files = os.listdir('./' + folder_name)
        myfiles = filter(lambda x: x.endswith(extension), files)
        posted_pic_list = [folder_name + '\\' + x for x in myfiles]
    except Exception:
        posted_pic_list = []

    bot = Bot()
    bot.login(username=login, password=password)

    for pic in posted_pic_list:
        caption = pic[:-4].split(' ')
        caption = ' '.join(caption[1:])
        timeout = random.randint(1, int(timeout_value * 0.5)) * timeout_value
        logging.info('timeout= ' + str(timeout))
        time.sleep(timeout)
        bot.upload_photo(pic, caption=caption)
        if bot.api.last_response.status_code is None:
            logging.info('response error! check the cookies! ' + str(
                bot.api.last_response))
        else:
            if bot.api.last_response.status_code != 200:
                raise ValueError('response error!')
