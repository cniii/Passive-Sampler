import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt
import tifffile as tiff

n_file = 1

filepath = "test_images/"
leftcard = "_left.TIF"
rightcard = "_right.TIF"
sample_1 = "_square.TIF"

normalized_value = np.empty([n_file,])

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


for j in range(n_file):
    # load images
    left = rgb2gray(tiff.imread(filepath + str(j+1) + leftcard))
    right = rgb2gray(tiff.imread(filepath + str(j+1) + rightcard))
    sample = rgb2gray(tiff.imread(filepath + str(j+1) + sample_1))
    #print(j)
    # plt.imshow(sample)
    # plt.show('hold')

    point = (sample[0, 0] + sample[0, round(sample.shape[0] / 2) - 1]
        + sample[round(sample.shape[1] / 2), 0] + sample[round(sample.shape[1] / 2), round(sample.shape[0]/ 2)]) / 4


    # get data points
    new_scale = np.empty([100, ])

    left_vertical = math.floor(left.shape[0] / 20)
    right_vertical = math.floor(right.shape[0] / 20)

    # get points from the image:
    for k in range(10):
        left_horizontal = math.floor(left.shape[1] / 10)
        right_horizontal = math.floor(right.shape[1] / 10)
        #print(left.shape[0])
        for h in range(5):
            new_scale[k * 10 + h] = left[left_vertical, left_horizontal]
            # print(left_horizontal, left_vertical)
            left_horizontal += math.floor(left.shape[1] / 5)
        for h in range(5, 10, 1):
            new_scale[k * 10 + h] = right[right_vertical, right_horizontal]
            right_horizontal += math.floor(right.shape[1] / 5)
        # print(left_horizontal)
        left_vertical += math.floor(left.shape[0] / 10)
        right_vertical += math.floor(right.shape[0] / 10)


    #normalize the greyscale
    y = np.linspace(100, 0, 100)
    scale = np.polyfit(new_scale, y, 1)

    fit = np.poly1d(scale)
    normalized_point = fit(point)
    #print for debugging
    # print(normalized_point)
    #print(new_scale)
    plt.plot(new_scale, y, 'ro', new_scale, fit(new_scale), "b-")
    plt.show('hold')
    print(point)
    print(normalized_point)

    #append to the array
    normalized_value[j,] = normalized_point
print(normalized_value)


