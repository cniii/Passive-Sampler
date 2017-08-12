import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt

filepath = "edge_detection_images/"
output = "precrop_images/"
suffix = ".JPG"
threshold = 50  # threshould for darkness
obviousness = 100  # number of the pixels that triggers the detection
n_file = 1

# edge detection


def find_line(vals):
    for i, tmp in enumerate(vals):
        tmp.sort()
        average = float(sum(tmp[:obviousness])) / len(tmp[:obviousness])
        if average <= threshold:
            return i
    return i

# get the outline of the target region


def find_border(img):
    width, height = img.size
    retval = [0, 0, width, height]

    pixels = list(img.getdata())
    vals = []  # store the value of the darkest color
    for pixel in pixels:
        vals.append(min(pixel))

    # make 2d array
    vals = np.array([vals[i * width:(i + 1) * width] for i in range(height)])

    # start with upper bounds
    forupper = vals.copy()
    retval[1] = find_line(forupper)

    # next, do lower bounds
    forlower = vals.copy()
    forlower = np.flipud(forlower)
    retval[3] = height - find_line(forlower)

    # left edge, same as before but roatate the data so left edge is top edge
    forleft = vals.copy()
    forleft = np.swapaxes(forleft, 0, 1)
    retval[0] = find_line(forleft)

    # and right edge is bottom edge of rotated array
    forright = vals.copy()
    forright = np.swapaxes(forright, 0, 1)
    forright = np.flipud(forright)
    retval[2] = width - find_line(forright)

    if retval[0] >= retval[2] or retval[1] >= retval[3]:
        print ("error, bounding box is not legit")
        return None
    return tuple(retval)


if __name__ == '__main__':
    for j in range(n_file):
        # image = Image.open(filepath + str(j + 1) + suffix)
        # box = find_border(image)
        # print ("result is: ", box)
        # result = image.crop(box)
        # result.show()
        # result.save("precrop_" + str(j + 1) + ".jpg")
        image = Image.open("precrop_1.jpg")
        box = find_border(image)
        result = image.crop(box)
        result.show()
