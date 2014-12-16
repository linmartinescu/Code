"""
    Author: Lindsay Martinescu
    Revised: Nov. 7 2014
    Objective: Take a photo and convert to a negative
    Imports: Open CV, Nump, sRGB2LMS(provided by Gabe Diaz)
"""

import cv2
import numpy as np 
import sRGB2LMS

def saveOutSML(imageIn, outFilePrefix):
    """
        Converts to LMS and saves as three seperate grayscale images
        Uses predefined names as according to handout
        Args:
            rgbImageIn is an image with 3 channels of color data.
            outFilePrefix is a string to be used as part of the output file name
    """
    LMSImg = sRGB2LMS.sRGB2LMS(imageIn)
    L,M,S = cv2.split(LMSImg)
    cv2.imwrite('{}-S.png'.format(outFilePrefix), S)
    cv2.imwrite('{}-M.png'.format(outFilePrefix), M)
    cv2.imwrite('{}-L.png'.format(outFilePrefix), L)
    
def rgbToNegative(rgbImageIn, outFilePrefix):
    """
        Calculates the negative of the image and save image
        Uses predefined names as according to handout
        Args:
            rgbImageIn is an RGB formatted image 
            outFilePrefix is a string to be used as part of the output file name
        Returns:
            The negative image 
    """
    negativeImage = np.full_like(rgbImageIn,256) - rgbImageIn
    cv2.imwrite('{}-Negative.png'.format(outFilePrefix), negativeImage)
    return negativeImage

def processColorImages(rgbImageFileName):
    """
        Calls functions to preform primary task (converting RGB image to negative)
        Uses predefined names as according to handout
        Args:
            rgbImageFileName is a string 
            outFilePrefix is a string to be used as part of the output file namee
    """
    rgbBaseImage = cv2.imread('{}.jpg'.format(rgbImageFileName), cv2.IMREAD_COLOR)
    cv2.imshow('image', rgbBaseImage)
    cv2.waitKey()
    saveOutSML('{}.jpg'.format(rgbImageFileName), '{}RGB'.format(rgbImageFileName))
    negativeImage = rgbToNegative(rgbBaseImage, rgbImageFileName)
    cv2.imshow('negative', negativeImage)
    cv2.waitKey()
    saveOutSML('{}-Negative.png'.format(rgbImageFileName), '{}Negative'.format(rgbImageFileName))

if __name__ == "__main__":
    processColorImages('negative_wolverine_3')
