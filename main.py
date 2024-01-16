from core.canny import getEdgesCanny

from inputmode.image import getSampleImages

# use sample image
img,img_gray = getSampleImages()

getEdgesCanny(img_gray)



if __name__=="__main__":
    print("main script")


