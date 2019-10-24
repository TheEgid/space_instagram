"""Main."""
import os
import sys
import logging
from dotenv import load_dotenv


from fetch_spacex import fetch_space_x_last_launch
from fetch_hubble import fetch_hubble_launch
from inst_post import inst_publish
from save_the_pictures import save_pictures


def inst_fetch_post(login, password, collection, folder_name='images',
                    extension='.jpg'):
    """Downloading and publishing."""
    save_pictures(fetch_space_x_last_launch(extension), folder_name=folder_name,
                  file_name='space', extension=extension)

    # save_pictures(fetch_hubble_launch(collection, extension), folder_name=folder_name,
    #               file_name='hubble', extension=extension)

    inst_publish(login=login, password=password, folder_name=folder_name,
                 extension=extension, timeout_value=7)


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.split(dir_path)[0])
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    LOGIN_INST = os.getenv("LOGIN_INST")
    PASSWORD_INST = str(os.getenv("PASSWORD_INST"))
    long_url = ''.join(sys.argv[1])  # 'wallpaper'
    inst_fetch_post(LOGIN_INST, PASSWORD_INST, long_url)
    logging.info('finished!')
