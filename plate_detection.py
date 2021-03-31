import cv2
from glob 						import glob
from os.path 					import splitext, basename
from src.utils 					import im2single
from src.keras_utils 			import load_model, detect_lp
from src.label 					import Shape, writeShapes
from hyperlpr import *

if __name__ == '__main__':
	imgs_paths = './car\\'
	print(imgs_paths)
	lp_threshold = .5
	f1 = open('carplate.txt','a')
	f2 = open('plate.txt', 'a')

	wpod_net_path = 'lp-detector/wpod-net.h5'
	wpod_net = load_model(wpod_net_path)

	for i in range(146):
		bname = imgs_paths+str(i)+'.png'
		print('\t Processing %s' % bname)
		#bname = splitext(basename(img_path))[0]
		img = cv2.imread(bname)
		if min(img.shape[:2]) != 0:
			ratio = float(max(img.shape[:2])) / min(img.shape[:2])
			side = int(ratio * 288.)
			bound_dim = min(side + (side % (2 ** 4)), 608)

			Llp, LlpImgs, _ = detect_lp(wpod_net, im2single(img), bound_dim, 2 ** 4, (240, 80), 0.5)
			if len(LlpImgs):
				print('%d,%d,%d,%d'%(int(Llp[0].pts[0][0] * img.shape[1]),int(Llp[0].pts[1][0] * img.shape[0]),int(Llp[0].pts[0][2] * img.shape[1]),int(Llp[0].pts[1][2] * img.shape[0])),file =f1)
				Ilp = LlpImgs[0]
				cv2.imwrite('./carplate/%s.png' % (i), Ilp * 255.)
				chars = HyperLPR_plate_recognition(Ilp * 255)

				if (len(chars) != 0):
					f2.write(chars[0][0])  # write the car plates
				else:
					f2.write('0')
				f2.write('\n')
			else:
				f1.write('0,0,0,0')
				f1.write('\n')
	f1.close()
	f2.close()