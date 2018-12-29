import requests
import os
from PIL import Image
from resizeimage import resizeimage
import logging
logging.basicConfig(level=logging.INFO)


def get_file_extension(url):
    """Get extension from url."""
    return '.' + str(url.split('.')[-1])


def save_picture(url, path):
    """Save image from path.
    
    Args:
        url(str): image link
        path(str): image file folder
        
    """

    dir_name = str(path.split('/')[0])

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    filename = path + get_file_extension(url)
    response = requests.get(url)

    if response.ok:
        with open(filename, 'wb') as f:
            f.write(response.content)
            logging.info('download & saved ' + filename)
        make_imageresize(filename)
    else:
        return None


def save_pictures(img_list, file_name='filename', folder_name='images'):
    """Enumeration & save all images in the list.
    
    Args:
	img_list(list): list contains images links
        file_name(str): pattern of the image file name
        folder_name(str): image file folder
        
    """
    
    if not isinstance(img_list, list):
        raise TypeError('incorrect img_list')
    for index, img in enumerate(img_list, 1):
        path = folder_name + '/'+ file_name + str(index)
        save_picture(img, path)

        
def make_imageresize(file_path, extension='.jpg'):
    """Resize images for standardized instagram posting.
    
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
        img.save(file_path, img.format)
        fd_img.close()
    else:
	pass
