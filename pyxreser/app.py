import argparse
import os
import shutil
import tempfile
import zipfile
from PIL import Image


def main():
    """
        Main function to parse command line arguments and call the appropriate function
    """
    try:
        parser = argparse.ArgumentParser(
            description='Pyxreser: Convert images (PNG,JPG,JPEG) to Pyxel .pyxres files')
        parser.add_argument('type', choices=[
                            'image'], help="Type of convertion. Currently, only 'image' file type is available for conversion.")
        parser.add_argument('number', type=int, choices=range(
            0, 7), default=0, help='Image number (0-7)')
        parser.add_argument('image', help='Input image file path')
        parser.add_argument(
            '-o', '--output', help='Output path and .pyxres file name')
        parser.add_argument('-v', '--version', action='version',
                            version='Pyxreser 1.0.0')
        args = parser.parse_args()
        new_file_created = False
        if not os.path.isfile(args.image):
            print('Error: Input image file not found.')
            return
        valid_extensions = '.png', '.jpg', '.jpeg'
        if not args.image.lower().endswith(valid_extensions):
            print('Error: Input file must be a PNG or JPEG image.')
            return
        image = Image.open(args.image)
        if image.size != (256, 256):
            print('Error: Input image must be 256x256 pixels.')
            return
        colors = set(image.getdata())
        if len(colors) > 16 or len(colors) == 16 and (0, 0, 0, 0) in colors:
            print('Error: Input image must have a maximum of 15 unique colors.')
            return
        color_char_map = {}
        for (idx, color) in enumerate(colors):
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color[:3])
            color_char_map[hex_color] = format(idx, 'x')
        if args.output is None:
            output_name = os.path.splitext(os.path.basename(args.image))[0]
        else:
            output_name = args.output
        if os.path.isfile(f"{output_name}.pyxres"):
            modify_existing_zip(output_name, args.number,
                                image, color_char_map)
        else:
            create_new_zip(output_name, args.number, image, color_char_map)
            new_file_created = True
        if new_file_created:
            print(
                f"Successfully created {output_name}.pyxres and {output_name}.pyxpal.")
    except Exception as e:
        print(f'An unexpected error has occurred :\n\n{e}')


def create_new_zip(output_name, number, image, color_char_map):
    """
        Create a new .pyxres file and .pyxpal file from the given image when the output file does not exist
    """
    colors = set(image.getdata())
    tilemap_filename = f"{output_name}{number}"
    generate_image(image, tilemap_filename, color_char_map)
    generate_pyxpal(colors, f"{output_name}.pyxpal")
    with open(f"tilemap{number}", 'w')as f:
        f.write('')
    with open('version', 'w')as f:
        f.write('1')
    zip_filename = f"{output_name}.pyxres"
    with zipfile.ZipFile(zip_filename, 'w')as zipf:
        zipf.write(tilemap_filename, arcname=os.path.join(
            'pyxel_resource', tilemap_filename))
        zipf.write(f"tilemap{number}", arcname=os.path.join(
            'pyxel_resource', f"tilemap{number}"))
        zipf.write('version', arcname=os.path.join(
            'pyxel_resource', 'version'))
    os.remove(tilemap_filename)
    os.remove(f"tilemap{number}")
    os.remove('version')


def modify_existing_zip(output_name, number, image, color_char_map):
    """
        Modify an existing .pyxres file and .pyxpal file from the given image when the output file already exists
    """
    zip_filename = f"{output_name}.pyxres"
    temp_dir = tempfile.mkdtemp(prefix='.temp_pyxreser')
    try:
        with zipfile.ZipFile(zip_filename, 'r')as existing_zip:
            existing_zip.extractall(temp_dir)
        tilemap_filename = f"{output_name}{number}"
        if tilemap_filename in existing_zip.namelist():
            os.remove(os.path.join(
                temp_dir, 'pyxel_resource', tilemap_filename))
        generate_image(image, os.path.join(
            temp_dir, 'pyxel_resource', tilemap_filename), color_char_map)
        image_filename = f"image{number}"
        image_path = os.path.join(temp_dir, 'pyxel_resource', image_filename)
        if os.path.isfile(image_path):
            shutil.move(os.path.join(temp_dir, 'pyxel_resource',
                        tilemap_filename), image_path)
        with open(os.path.join(temp_dir, 'pyxel_resource', f"tilemap{number}"), 'w')as f:
            f.write('')
        with zipfile.ZipFile(zip_filename, 'w')as new_zip:
            for (root, _, files) in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    new_zip.write(file_path, arcname=arcname)
        colors = set(image.getdata())
        generate_pyxpal(colors, f"{output_name}.pyxpal")
        print(f"Successfully updated {zip_filename}.")
    finally:
        shutil.rmtree(temp_dir)


def generate_pyxpal(colors, filename):
    """
        Generate a .pyxpal file from the given colors
    """
    with open(filename, 'w')as f:
        for color in sorted(colors):
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color[:3])
            f.write(hex_color[1:]+'\n')


def generate_image(image, filename, color_char_map):
    """
        Generate a image file from the given image
    """
    with open(filename, 'w')as f:
        for y in range(image.height):
            for x in range(image.width):
                pixel = image.getpixel((x, y))
                if pixel[3] == 0:
                    hex_color = '#000000'
                else:
                    hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel[:3])
                f.write(color_char_map.get(hex_color, '5'))
            f.write('\n')


if __name__ == '__main__':
    main()
