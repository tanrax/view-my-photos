# View my photos

Generator of static galleries. Indicate which is your folder with the images and relax.
The objective of this software is to be able to visualize a great quantity of images comfortably (photos of your vacations, you your children, enemies, etc). Although it can be used to build a section within a website.

<p align="center">
    <img src="https://min.gitcdn.link/repo/tanrax/view-my-photos/master/demo.jpg">
</p>

## Use

```bash
view-my-photos --path [Path photos] --thumbnails_path [Path where the thumbnails will be stored] [--ignore [Path to ignore]]
```

## Example

### Basic

```bash
view-my-photos --path trip_spain --thumbnails_path .
```

### Ignore folder

```bash
view-my-photos --path family --thumbnails_path .  --ignore ex-girlfriend
```

## Install

Requires Python3.6 or higher. 

``` bash
pip3 install --user view-my-photos
```

### Only Debian/Ubuntu

``` bash
sudo apt install libjpeg8-dev zlib1g-dev
```

## Update

``` bash
pip3 install --user --upgrade view-my-photos
```
