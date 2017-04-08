import os

import numpy as np
from scipy import misc, ndimage
from skimage import exposure

__author__ = 'Daniel'


class Scanifier(object):
    def run(self, imgin_path, imgout_path=None, increase_exposure=False):
        imgin_path = self.__expand_user(imgin_path)
        img = misc.imread(imgin_path)

        img_blurred = self.__blur(img)
        img = self.__divide(img, img_blurred)
        if increase_exposure:
            img = exposure.adjust_sigmoid(img)

        if not imgout_path:
            imgout_path = self.__add_suffix(imgin_path)
        misc.imsave(imgout_path, img)
        print("Saved to", imgout_path)

    def __expand_user(self, path):
        if path.startswith('~/'):
            return os.path.join(os.path.expanduser('~'), path[2:])
        return path

    def __add_suffix(self, path):
        name, ext = os.path.splitext(path)
        return "{name}_{suffix}{ext}".format(name=name, suffix="scanify",
                                             ext=ext)

    def __blur(self, img):
        """
        Gaussian blur
        """
        print("Gaussian Filtering")
        return ndimage.gaussian_filter(img, sigma=100)

    def __divide(self, a, b):
        """
        divide blend
        """
        print("Divide Blending")
        c = a / ((b.astype('float') + 1) / 256)
        d = c * (c < 255) + 255 * np.ones(np.shape(c)) * (c > 255)
        e = d.astype('uint8')
        return e

if __name__ == "__main__":
    scanifier = Scanifier()
    ret1 = scanifier.run('~/Desktop/p0.jpg')