# Importing glob & OpenCv Modules.
import glob
import cv2 as cv


# Reads png files and converts them into B&W jpg.
def convert_image():
    for png_img in glob.glob('images/*.png'):
        read_image = cv.imread(png_img,0)
        cv.imwrite(png_img[:-3]+'jpg',read_image)


# Function call.
if __name__ == "__main__":
    convert_image()
