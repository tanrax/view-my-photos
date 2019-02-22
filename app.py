import click
import os
import PIL
from PIL import Image
import hashlib

# Variables
FORMATS_PHOTOS = ('jpg', 'jpeg', 'png', 'gif')
THUMBNAIL_WIDTH = 400
BLOCKSIZE_SHA1 = 65536

@click.command()
@click.option('--path', required=True, help='Folder path with your photos', type=click.Path(exists=True))
@click.option('--thumbnails', required=True, help='Where the thumbnails will be saved', type=click.Path(exists=True))
def main(path, thumbnail_path):
    photos = search_photos(path)
    for photo in photos:
        save_thumbnail(photo, thumbnail_path)

def search_photos(path):
    ''' Search all images path '''
    paths_photos = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(extensions):
                # Save path
                paths_photos.append(os.path.join(root, file))
    return paths_photos

def save_thumbnail(file_original, path_folder_thumbnails):
    ''' Make and save thumbnail '''
    img = Image.open(file_original)
    wpercent = (THUMBNAIL_WIDTH / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((THUMBNAIL_WIDTH, hsize), PIL.Image.ANTIALIAS)
    img.save(os.path.join(path_folder_thumbnails, get_sha1_hash(file_original)))

def get_sha1_hash(file)
    ''' Get sha1 from file '''
    hasher = hashlib.sha1()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE_SHA1)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE_SHA1)
    return hasher.hexdigest()

if __name__ == '__main__':
    main()
