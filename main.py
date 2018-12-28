import os
import sys
from dotenv import load_dotenv

dir_path = os.path.dirname(os.path.realpath(__file__)) #+paths
sys.path.insert(0, os.path.split(dir_path)[0])

from space_instagram.fetch_spacex import fetch_space_x_last_launch
from space_instagram.fetch_hubble import fetch_hubble_launch
from space_instagram.inst_post import inst_publication


def inst_fetch_post():
 
    pass
    
    
    
if __name__ == '__main__':
    load_dotenv()
    LOGIN_INST = os.getenv("LOGIN_INST")
    PASSWORD_INST = str(os.getenv("PASSWORD_INST"))

    #fetch_space_x_last_launch()

    #fetch_hubble_launch('printshop') #wallpaper

    inst_publication(LOGIN_INST, PASSWORD_INST)

    print('Done!')
