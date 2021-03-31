from glob 						import glob
from os.path 					import splitext, basename
import cv2

if __name__ == '__main__':
    imgs_paths = glob('./car/car*.png')
    for i, img_path in enumerate(imgs_paths):
        bname = splitext(basename(img_path))[0]
        bname = bname[3:]
        img = cv2.imread(img_path)
        cv2.imwrite('./car1/%s.png' % (bname),img)