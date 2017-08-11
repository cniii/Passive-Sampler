import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt
import tifffile as tiff

n_file = 10

filepath = "test_images/"
leftcard = "_left.TIF"
rightcard = "_right.TIF"
sample_1 = "_square.TIF"

normalized_value = np.empty([n_file, ])
points = np.empty([n_file, ])


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


for j in range(n_file):
    # load images
    left = rgb2gray(tiff.imread(filepath + str(j + 1) + leftcard))
    right = rgb2gray(tiff.imread(filepath + str(j + 1) + rightcard))
    sample = rgb2gray(tiff.imread(filepath + str(j + 1) + sample_1))
    # print(j)
    # plt.imshow(sample)
    # plt.show('hold')

    dim1 = sample.shape[0]
    dim2 = sample.shape[1]

    sample_center = sample[round(dim1 / 5): round(dim1 * 4 / 5), round(dim2 / 5): round(dim2 * 4 / 5)]

    dim1 = sample_center.shape[0]
    dim2 = sample_center.shape[1]

    point = np.sum(sample_center) / (dim1 * dim2)

    # get data points
    new_scale = np.empty([100, ])

    left_vertical = math.floor(left.shape[0] / 20)
    right_vertical = math.floor(right.shape[0] / 20)

    # get points from the image:
    for k in range(10):
        left_horizontal = math.floor(left.shape[1] / 10)
        right_horizontal = math.floor(right.shape[1] / 10)
        # print(left.shape[0])
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

    # normalize the greyscale
    y = np.linspace(100, 0, 100)
    scale = np.polyfit(new_scale, y, 1)

    fit = np.poly1d(scale)
    normalized_point = fit(point)
    # print for debugging
    '''
    print(normalized_point)
    print(new_scale)
    plt.plot(new_scale, y, 'g.', new_scale, fit(new_scale), "b-", point, normalized_point, 'ro')
    plt.show('hold')
    print(point)
    print(normalized_point)
    '''

    # append to the array
    points[j, ] = point
    normalized_value[j, ] = normalized_point
print("Before normalized:" + str(points));
print("before variance:" + str(np.var(points)))
print("After normalized:" + str(normalized_value))
print("aftervariance:" + str(np.var(normalized_value)))
