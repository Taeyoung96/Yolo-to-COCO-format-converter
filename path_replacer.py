import os
import glob
import argparse

parser = argparse.ArgumentParser(description="Bu Python dosyasi elimizdeki yolo formatinda elde edilen ciktilarin json formatina donusumu icin on hazirlik yapmaktadir.")
parser.add_argument('-i','--path_image_folder',help="Gorsellerin bulundugu dosya yolunu giriniz.",type=str)
parser.add_argument('-p','--path_txt',help="Olusturmak istenen 'txt' dosyasinin dosya yolunu giriniz.",type=str)
args = parser.parse_args()
def replacer(image_folder, path_txt):
    path = os.path.abspath(image_folder)
    f = open(path_txt, "r+")

    for i in glob.glob(path + "/*.jpg"):
        f.write(i+ "\n")

    f.close()

if __name__ == '__main__':
    replacer(args.path_image_folder, args.path_txt)
    