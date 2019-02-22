import click
import os
import PIL
from PIL import Image
import hashlib
import ntpath

# Variables
FORMATS_PHOTOS = ('jpg', 'jpeg', 'png', 'gif')
THUMBNAIL_WIDTH = 400
BLOCKSIZE_SHA1 = 65536
thumbnails = []

@click.command()
@click.option('--path', required=True, help='Folder path with your photos', type=click.Path(exists=True))
@click.option('--thumbnails_path', required=True, help='Where the thumbnails will be saved', type=click.Path(exists=False))
def main(path, thumbnails_path):
    # Make thumbnails
    photos = search_photos(path)
    for photo in photos:
        save_thumbnail(photo, thumbnails_path)

def search_photos(path):
    ''' Search all images path '''
    paths_photos = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(FORMATS_PHOTOS):
                # Save path
                paths_photos.append(os.path.join(root, file))
    return paths_photos

def save_thumbnail(file_original, path_folder_thumbnails):
    ''' Make and save thumbnail '''
    # Create folder thumbnails
    if not os.path.exists(path_folder_thumbnails):
        os.makedirs(path_folder_thumbnails)
    # Resize image
    final_path = os.path.join(path_folder_thumbnails, get_filename_with_sha1(file_original))
    if not os.path.isfile(final_path):
        img = Image.open(file_original)
        wpercent = (THUMBNAIL_WIDTH / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((THUMBNAIL_WIDTH, hsize), PIL.Image.ANTIALIAS)
        # Save image in folder
        img.save(final_path)
    # Save image in dict
    thumbnails.append({
            'url': final_path,
            'original': file_original
        })

def get_sha1_hash(file):
    ''' Get sha1 from file '''
    hasher = hashlib.sha1()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE_SHA1)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE_SHA1)
    return hasher.hexdigest()

def get_filename_with_sha1(file):
    return get_sha1_hash(file) + ntpath.basename(file)

if __name__ == '__main__':
    main()
