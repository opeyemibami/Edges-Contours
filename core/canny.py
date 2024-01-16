import cv2 as cv
import pathlib 
import numpy as np


def main():
    base_dir = pathlib.Path(__file__).parents[1]
    sampleImg_path = str(base_dir.joinpath("data","sample","sampleImage.jpg"))  
    img_gray = cv.imread(sampleImg_path,cv.IMREAD_GRAYSCALE)
    # edge detection
    img_edge = cv.Canny(img_gray,130,170)
    # dilate
    img_edge_dilate = cv.dilate(img_edge,np.ones((3,3),dtype=np.int8))
    # Erode 
    img_edge_erode = cv.erode(img_edge_dilate,np.ones((3,3),dtype=np.int8))

    cv.imshow("img_edge",img_edge)
    cv.imshow("img_edge_dilate",img_edge_dilate)
    cv.imshow("img_edge_erode",img_edge_erode)
    cv.waitKey(0)

    return

def getEdgesCanny(img_gray=None):
    if img_gray==None:
        print()

    # edge detection
    img_edge = cv.Canny(img_gray,130,170)
    # dilate
    img_edge_dilate = cv.dilate(img_edge,np.ones((3,3),dtype=np.int8))
    # Erode 
    img_edge_erode = cv.erode(img_edge_dilate,np.ones((3,3),dtype=np.int8))

    cv.imshow("img_edge",img_edge)
    cv.imshow("img_edge_dilate",img_edge_dilate)
    cv.imshow("img_edge_erode",img_edge_erode)
    cv.waitKey(0)
    return

if __name__=="__main__":
    main()


