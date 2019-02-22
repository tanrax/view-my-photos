import click
import os
import PIL
from PIL import Image

# Variables
FORMATS_PHOTOS = ('jpg', 'jpeg', 'png', 'gif')
THUMBNAIL_WIDTH = 400

@click.command()
@click.option('--path', required=True, help='Folder path with your photos', type=click.Path(exists=True))
@click.option('--thumbnails', required=True, help='Where the thumbnails will be saved', type=click.Path(exists=True))
def main(path, thumbnail_path):
    photos = search_photos(path)

def search_photos(path):
    ''' Search all images path '''
    paths_photos = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(extensions):
                # Save path
                paths_photos.append(os.path.join(root, file))
    return paths_photos

def make_thumbnail(path_original, path_folder_thumbnails):
    img = Image.open(‘fullsized_image.jpg')
    wpercent = (THUMBNAIL_WIDTH / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((THUMBNAIL_WIDTH, hsize), PIL.Image.ANTIALIAS)
    img.save(‘resized_image.jpg')

if __name__ == '__main__':
    main()
