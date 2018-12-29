"""Main."""
import os
import sys
from dotenv import load_dotenv

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.split(dir_path)[0])

from space_instagram.fetch_spacex import fetch_space_x_last_launch
from space_instagram.fetch_hubble import fetch_hubble_launch
from space_instagram.inst_post import inst_publish
from space_instagram.save_the_pictures import save_pictures


def inst_fetch_post(login, password, folder_name, extension, collection):
    """Downloading and publishing."""
    save_pictures(fetch_space_x_last_launch(), folder_name=folder_name,
                  file_name='space', extension=extension)

    save_pictures(fetch_hubble_launch(collection), folder_name=folder_name,
                  file_name='hubble', extension=extension)

    inst_publish(login=login, password=password, folder_name=folder_name,
                 extension=extension, timeout_value=7)


if __name__ == '__main__':
    load_dotenv()
    LOGIN_INST = os.getenv("LOGIN_INST")
    PASSWORD_INST = str(os.getenv("PASSWORD_INST"))
    inst_fetch_post(LOGIN_INST, PASSWORD_INST, 'images', '.jpg', 'wallpaper')
