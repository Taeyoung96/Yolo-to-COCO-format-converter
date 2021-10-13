"""
Only use this module if you want to retain a text file artifact which
lists all image names.

If you do not need to retain this artifact, you can just call main.py
passing in the directory which contains all of the images via the --path
parameter, instead of passing it a text file which lists all of the image
file paths.

"""
import os
import glob
import argparse

parser = argparse.ArgumentParser(
    description="This Python file makes preliminary preparations for the conversion of the outputs obtained in the yolo format to json format."
)
parser.add_argument(
    "-i",
    "--path_image_folder",
    help="Enter the file path where the images are located.",
    type=str,
)
parser.add_argument(
    "-p",
    "--path_txt",
    help="Enter the file path of the 'txt' file you want to create.",
    type=str,
)
args = parser.parse_args()


def replacer(image_folder, path_txt):
    path = os.path.abspath(image_folder)
    f = open(path_txt, "w")

    for i in glob.glob(path + "/*.jpg"):
        f.write(i + "\n")
    print('----File ".txt" created successfully----')
    f.close()


if __name__ == "__main__":
    replacer(args.path_image_folder, args.path_txt)
