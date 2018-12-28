import requests
from .save_the_pictures import save_pictures
import logging

logging.basicConfig(level=logging.INFO)

'''
Hubble program

'''

def extract_hubble_collection(collection):
    id_list = []
    _url ='http://hubblesite.org/api/v3/images/' + collection
    response = requests.get(_url)
    if response.ok:
        fetch = response.json()
        for img in fetch:
            id_list.append(img['id'])
        return id_list
    else:
        return None

def extract_fetch_hubble(id_list):
    img_list = []
    for id in id_list:
        _url ='http://hubblesite.org/api/v3/image/' + str(id)
        response = requests.get(_url)
        if response.ok:
            img = response.json()['image_files'][-1]
            img_list.append(img['file_url'])
        else:
            logging.info('No photos now')
            return None
    return img_list


def fetch_hubble_launch(collection):
    collections_list = extract_hubble_collection(collection)
    images_list = extract_fetch_hubble(collections_list)
    save_pictures(images_list)