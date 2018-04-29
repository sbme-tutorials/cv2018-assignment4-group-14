import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

#By El mo3eed

def otsuThresholdB(image):
    #Get size of image
    rows, cols =  image.shape
    #Plotting image histogram
    plt.figure()
    #We are interested on H (histogram), other values that plt.hist returns will be ignored here
    H, binEdges, patches = plt.hist(image.ravel(),256)
    # Getting relative histogram (pdf)
    pdf = H /(rows*cols)
    # Get cdf for all gray levels
    cdf = np.cumsum(pdf)
    #Initialization
    othresh = 1
    maxVarB = 0
    for t in range(1, 255):
        # gray levels belongs to background
        bg = np.arange(0, t)
        # object gray levels
        obj = np.arange(t, 256)
        # Calculation of mean gray level for object and background
        mBg = sum(bg * pdf[0:t]) / cdf[t]
        mObj = sum(obj * pdf[t:256]) / (1 - cdf[t])
        # Calculate between class variance ==> Which should be maximumized
        varB = cdf[t] * (1 - cdf[t]) * (mObj - mBg) ** 2
        # Pick up max variance and corresponding threshold
        if varB > maxVarB:
            maxVarB = varB
            othresh = t
    print othresh
    return othresh

def binarize( gray_image , threshold ):
    return 1 * ( gray_image > threshold )

#Read an image
image = plt.imread('images/Pyramids2.jpg')
#Extract value channel (intensity)
hsvImage = colors.rgb_to_hsv(image)
myIm = hsvImage[...,2]
#Show original image
plt.figure()
plt.imshow(myIm)
plt.set_cmap("gray")
plt.suptitle('Original Image')
plt.title('Original Image')
#Get optimal threshold
oTb = otsuThresholdB(myIm)
#Binarize the image and show it
binaryIm = binarize(myIm, oTb)
plt.figure()
plt.imshow(binaryIm)
plt.title('Binarize after thresholding with Ostu')
plt.suptitle('It doesnot actually Binarized Beacuse of Python')
plt.show()