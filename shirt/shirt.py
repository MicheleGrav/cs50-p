from PIL import Image, ImageOps
import sys
import os

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_file output_file")

    in_name = sys.argv[1].lower()
    out_name = sys.argv[2].lower()

    if not is_image_file(in_name):
        sys.exit("Not an image")

    if not is_image_file(out_name):
        sys.exit("Not an image")

    if not is_same_ext(in_name, out_name):
        sys.exit("Not same extension")

    if not os.path.isfile(in_name):
        sys.exit("File does not exist")

    input_img = Image.open(in_name)

    shirt = Image.open("shirt.png")

    input_img = ImageOps.fit(input_img, shirt.size)

    input_img.paste(shirt, shirt)

    input_img.save(out_name)

    print("Image saved")


def is_image_file(filename):
    _, ext = os.path.splitext(filename)

    return ext in ['.jpg', '.jpeg', '.png']


def is_same_ext(file1, file2):
    _, ext1 = os.path.splitext(file1)
    _, ext2 = os.path.splitext(file2)

    return ext1 == ext2

if __name__ == "__main__":
    main()

