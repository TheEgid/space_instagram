"""Get from SPACE X."""
import requests
import logging


def fetch_space_x_last_launch(extension):
    """Fetch links of images from SpaceX website.

    http://www.spacex.com/
    Returns:
        id_list(list): the list of urls for images
    """
    response = requests.get('https://api.spacexdata.com/v3/launches/latest',
                            verify=False)
    if response.ok:
        fetch_json = response.json()
        img_list = fetch_json['links']['flickr_images']
        if img_list:
            img_list = [url for url in img_list if url.endswith(extension)]
            return img_list
        else:
            logging.info('no images now')
            return None
    else:
        return None
