import cv2 as cv
import pathlib
base_dir = pathlib.Path(__file__).parents[1]
sampleimage_path = str(base_dir.joinpath('data','sample','sampleImage.jpg'))
# print("#######################: ",sampleimage_path)

    
def getSampleImages():
    """
    return: sample image in BGR colorspace, sample image in Grayscale
    """
    img = cv.imread(sampleimage_path)
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return img,img_gray

def imageUpload():
    # TODO: "use streamlit to handle image upload"
    img,img_gray = None
    return img,img_gray
    