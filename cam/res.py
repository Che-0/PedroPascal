import cv2 as cv

def changesRes(width, height):
    #solo funciona con live video
    capture.set(3, width) 
    capture.set(4, height)