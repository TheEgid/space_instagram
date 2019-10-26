"""Saving the download from websites images."""
import requests
import os
from PIL import Image
from resizeimage import resizeimage
import logging


class SpaceReturnEmptyImgList(Exception):
    """Declare special exception."""
    pass


def get_file_extension(url):
    """Get extension from url."""
    return '.' + url.split('.')[-1]


def get_path(file):
    module_dir = os.path.dirname(__file__)
    return os.path.join(module_dir, file)


def convert_to_jpg(file):
    file = get_path(file)
    file_name, file_extension = os.path.splitext(file)
    if file_extension.lower() != 'jpg':
        logging.info(f' Process with {file_name}{file_extension}')
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        file = f'{file_name}.jpg'
        rgb_im.save(file)
    return file


def save_picture(url, path):
    filename = path + get_file_extension(url)
    dir_name = path.split('/')[0]
    os.makedirs(dir_name, exist_ok=True)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    global file_path
    try:
        with open(filename, 'wb') as f:
            f.write(response.content)
        file_path = convert_to_jpg(filename)
        make_imageresize(file_path)
        logging.info(f' Downloaded & saved & resized {file_path}')

    except IOError:
        pass


def save_pictures(img_list, folder_name, file_name, extension):
    """Enumeration & save all images in the list.
    
    Args:
        img_list(list): list contains images links
        file_name(str): pattern of the image file name
        folder_name(str): image file folder
    """

    if not isinstance(img_list, list):
        raise SpaceReturnEmptyImgList()

    for index, img in enumerate(img_list, 1):
        path = f'{folder_name}/{file_name}{index}'
        save_picture(img, path)


def make_imageresize(file_path, extension='.jpg'):
    """Resize images for standardized instagram posting and overwrite their.

    Args:
        file_path(str): image file location
        extension(str): image file extension
    """
    gorizontal = [1080, 565]
    vertical = [600, 750]
    quadrate = [gorizontal[0], gorizontal[0]]

    if get_file_extension(file_path) == extension:
        fd_img = open(file_path, 'rb')

        img = Image.open(fd_img)

        try:
            if img.width > img.height:
                img = resizeimage.resize_contain(img, gorizontal)
            elif img.width == img.height:
                img = resizeimage.resize_contain(img, quadrate)
            else:
                img = resizeimage.resize_contain(img, vertical)
        except resizeimage.ImageSizeError:
            logging.info('ImageSizeError' + img)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(file_path, img.format)

        fd_img.close()
    else:
        pass
