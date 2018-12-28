import requests
from .save_the_pictures import save_pictures
import logging
logging.basicConfig(level=logging.INFO)


def extract_fetch_space_x():
    """Fetch list of images from SpaceX website.
    http://www.spacex.com/

    Returns:
        fetch(list)

    """
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')
    if response.ok:
        fetch_json = response.json()
        fetch = fetch_json['links']['flickr_images']
        if fetch:
            return fetch
        else:
            logging.info(u'No photos now')
            raise SystemExit()
    else:
        return None

def fetch_space_x_last_launch():
    """Save images of last launch from SpaceX website.
	http://www.spacex.com/

    """
    save_pictures(extract_fetch_space_x())
