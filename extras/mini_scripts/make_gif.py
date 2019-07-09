"""

Designed and Developed by-
Udayraj Deshmukh 
https://github.com/Udayraj123

"""
import glob
from PIL import Image, ExifTags
# in_dir = '../../outputs/checkedOMRs/'
in_dir = 'inputs/'


def resize_util(img, u_width, u_height=None):
    if u_height == None:
        h,w=img.shape[:2]
        u_height = int(h*u_width/w)
    return cv2.resize(img,(u_width,u_height))

GAP = 1500 #ms
dims = (400, 400)
# dims = [500, 400]
im1 = Image.open("inputs/gif/inputs_mobile.jpg").resize(dims)
# im1 = Image.open("inputs/gif/xeroxed_mobile.jpg").resize(dims)

for suffix1 in ["JE/","HE/"]:#,"JH/","HH/"]:
	for suffix2 in [""]:#,"_MULTI_/","_BADSCAN_/"]:
		dir_glob =in_dir+suffix1 + suffix2+'*.jpg'
		allOMRs= sorted(list(glob.iglob(dir_glob)))
		if(len(allOMRs)):
			# append_images= [im1,im1] + [Image.open(filepath).resize(dims) for filepath in allOMRs]
			append_images= [] 
			for i, filepath in enumerate(allOMRs):
				img = Image.open(filepath)
				if(i % 2 == 0):
					img = img.rotate(270)

				# print(img._getexif().items())
				append_images.append(img.resize(dims))
			filename = "outputs/gif/checking_"+suffix1[:-1] + suffix2+".gif"
			im1.save(filename, save_all=True, append_images=append_images, duration=GAP*(2 if len(suffix2) else 1), loop=0)
			print("Saved : "+filename)
		else:
			print("Empty glob: "+dir_glob)



"""
import cv2
y = cv2.imread("gif_start.jpg")
z = cv2.resize(cv2.GaussianBlur(y[:y.shape[1]//2,:], (25, 25), 0), (800,600))
label = "Template Alignment"
pos = (80,300)
cv2.putText(z,label,pos,cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 6)
cv2.imwrite("template_alignment.jpg",z)
"""