import sys
from PIL import Image
import glob
import os
import argparse


def main():


    parser = argparse.ArgumentParser(
                    prog = 'Webp-B-Gone',
                    description = 'Converts all .webp files in designated folder and sub-folders \
                                    into .jpg or .png files based on input option')
    parser.add_argument('extension', choices=['jpg', 'png'], metavar='extension', help='file type to convert to (jpg or png)')
    # 'keep' is not used in the code but this argument forces a choice to keep or remove and has no default value
    parser.add_argument('fate', choices=['remove', 'keep'], metavar='fate', help='remove or keep old webp files after \
                            jpg/png version created (remove or keep)')
    parser.add_argument('path', metavar='path', help='full path to top level folder that holds webp files to convert')
    args = parser.parse_args()

    extension = args.extension
    fate = args.fate
    path = args.path

    # glob.glob will recursively search sub-folders for all webp files
    for file in glob.glob(path + '/**/*.webp', recursive=True):
        try:
            pic = Image.open(file, mode='r').convert('RGB')
        except OSError:
            # Will skip over files that raise OSError so that all the rest of the webp files can still be converted
            print(f'an OSError has occurred for {file}')
            continue

        if extension == ('jpg'):
            pic.save(file.replace('.webp', '.jpg'), format='jpeg')
            if fate == 'remove':
                os.remove(file)
        elif extension == ('png'):
            pic.save(file.replace('.webp', '.png'), format='png')
            if fate == 'remove':
                os.remove(file)
        else:
            sys.exit('An error has occurred.')


if __name__ == "__main__":
    main()


