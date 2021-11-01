import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class ImgProcessing:
    @staticmethod
    def image_load(img_name):
        # Use a breakpoint in the code line below to debug your script.
        pic = Image.open(img_name)
        pix_mat = np.array(pic)
        return pix_mat

    #save as png file
    @staticmethod
    def image_save(img_name, pixel_array):
        img = Image.fromarray(pixel_array, 'L')
        img.save(img_name)

    @staticmethod
    def print_img(pixel_mat):
        plt.figure()
        plt.imshow(pixel_mat)
        plt.colorbar()
        plt.grid(False)
        plt.show()

    @staticmethod
    def print_img_list(original, corrupted, reconsted, c_rate):
        plt.figure(figsize=(10, 3))

        plt.subplot(1, 3, 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(original, cmap=plt.cm.binary)
        plt.xlabel("original")

        plt.subplot(1, 3, 2)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(corrupted, cmap=plt.cm.binary)
        label_format = "corrupted (rate: {c_rate:.2f})"
        label_str = label_format.format(c_rate=c_rate)
        plt.xlabel(label_str)

        plt.subplot(1, 3, 3)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(reconsted, cmap=plt.cm.binary)
        plt.xlabel("reconsted")

        plt.show()



