import click
import os
import PIL
from PIL import Image
import hashlib
import ntpath
import json

# Variables
FORMATS_PHOTOS = ('jpg', 'jpeg', 'png', 'gif')
THUMBNAIL_WIDTH = 400
THUMBNAIL_FOLDER_NAME = 'thumbnails'
BLOCKSIZE_SHA1 = 65536
FILENAME_JSON = 'data.json'
thumbnails = []

@click.command()
@click.option('--path', required=True, help='Folder path with your photos', type=click.Path(exists=True))
@click.option('--thumbnails_path', required=True, help='Where the thumbnails will be saved', type=click.Path(exists=False))
@click.option('--ignore', help='Path ignore', type=click.Path(exists=True))
def main(path, thumbnails_path, ignore):
    ''' Main '''
    # Make thumbnails
    click.echo(click.style('Make thumbnails'))
    photos = search_photos(path, ignore)
    with click.progressbar(photos) as photos_progress:
        for photo in photos_progress:
            save_thumbnail(photo, thumbnails_path)
    # Delete old thumbnails
    click.echo(click.style('Delete old thumbnails'))
    remove_old_thumbnails(thumbnails_path, thumbnails)
    # Save JSON
    click.echo(click.style('Save data'))
    save_json(thumbnails, FILENAME_JSON)
    click.echo(click.style('Done!', fg='green'))

def search_photos(path, path_ignore):
    ''' Search all images path '''
    paths_photos = []
    for root, dirs, files in os.walk(path):
        if not path_ignore or path_ignore not in root:
            for file in files:
                if file.lower().endswith(FORMATS_PHOTOS):
                    # Save path
                    paths_photos.append(os.path.join(root, file))
    return paths_photos

def save_thumbnail(file_original, path_folder_thumbnails):
    ''' Make and save thumbnail '''
    # Create folder thumbnails
    if not os.path.exists(os.path.join(path_folder_thumbnails, THUMBNAIL_FOLDER_NAME)):
        os.makedirs(os.path.join(path_folder_thumbnails, THUMBNAIL_FOLDER_NAME))
    # Resize image
    final_name = get_filename_with_sha1(file_original)
    final_path = os.path.join(path_folder_thumbnails, THUMBNAIL_FOLDER_NAME, final_name)
    if not os.path.isfile(final_path):
        img = Image.open(file_original)
        wpercent = (THUMBNAIL_WIDTH / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((THUMBNAIL_WIDTH, hsize), PIL.Image.ANTIALIAS)
        # Save image in folder
        img.save(final_path)
    # Save image in dict
    thumbnails.append({
            'name': final_name,
            'original': file_original,
            'date': int(os.path.getmtime(file_original))
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
    ''' Get filename with sha1 '''
    return get_sha1_hash(file) + ntpath.basename(file)

def remove_old_thumbnails(thumbnails_path, thumbnails):
    ''' Remove from folder thumnails old images '''
    # Read folder
    for root, dirs, files in os.walk(os.path.join(thumbnails_path, THUMBNAIL_FOLDER_NAME)):
        # Read files
        for file in files:
            # Check file in dict
            exist = False
            for item in thumbnails:
                if item['name'] == file:
                    exist = True
            # Delete file
            if not exist:
                os.remove(os.path.join(thumbnails_path, THUMBNAIL_FOLDER_NAME, file))

def save_json(thumbnails, filename):
    ''' Print dict to JSON '''
    with open(filename, 'w') as fp:
        json.dump(thumbnails, fp)

if __name__ == '__main__':
    main()

