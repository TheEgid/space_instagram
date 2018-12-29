"""Get from Hubble."""
import requests
from .save_the_pictures import save_pictures
import logging

logging.basicConfig(level=logging.INFO)


def extract_hubble_collection(collection):
    """Extract particular collection of images from Hubble website.

    http://hubblesite.org
    Args:
        collection(str): the name of collection on the website
    Returns:
        id_list(list): the list of images ID
    """
    id_list = []
    _url = 'http://hubblesite.org/api/v3/images/' + collection
    response = requests.get(_url)
    if response.ok:
        fetch = response.json()
        for img in fetch:
            id_list.append(img['id'])
        return id_list
    else:
        return None


def extract_urls_images_hubble(id_list):
    """Extract image links.

    Args:
        id_list(list): the list of images ID
    Returns:
        id_list(list): the list of urls for images
    """
    img_list = []
    for id in id_list:
        _url = 'http://hubblesite.org/api/v3/image/' + str(id)
        response = requests.get(_url)
        if response.ok:
            img = response.json()['image_files'][-1]
            img_list.append(img['file_url'])
        else:
            logging.info('no images now')
            return None
    return img_list


def fetch_hubble_launch(collection):
    """Save images of different collections from Hubble website.

    http://hubblesite.org
    Args:
        collection(str): the name of collection on the website
    Returns:
        id_list(list): the list of urls for images
    """
    collections_list = extract_hubble_collection(collection)
    images_list = extract_urls_images_hubble(collections_list)
    return images_list
