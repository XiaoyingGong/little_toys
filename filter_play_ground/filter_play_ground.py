# author: 龚潇颖(Xiaoying Gong)
# date： 2020/6/27 15:19  
# IDE：PyCharm 
# des:手写的卷积操作
# （h_in - h_filter + 1） / stride
# input(s)：
# output(s)：
import numpy as np
import matplotlib.pyplot as plt

def conv(img, filters, stride):
    img_h = img.shape[0]
    img_w = img.shape[1]
    img_c = img.shape[2]


    filter_h = filters[0].shape[0]
    filter_w = filters[0].shape[1]


    filter_num = len(filters)

    h_out = int(np.ceil((img_h - filter_h + 1) / stride))
    w_out = int(np.ceil((img_w - filter_w + 1) / stride))

    img_out = np.zeros((h_out, w_out, filter_num))

    for i in range(h_out):
        for j in range(h_out):
            for k in range(filter_num):
                img_cur = img[i:i+filter_h, j:j+filter_w, :]
                conv_cur = np.dot(img_cur.flatten(), filters[k].flatten().T)
                img_out[i, j, k] = conv_cur
    return img_out

img = plt.imread('F:/mySrc/pycharm/little_toys/filter_play_ground/img/UJ21S{W`H1F(OH7V~E`DV%X.jpg')

filter_w = 5
filter_h = 5
filter_c = 3
filters = []

for i in range(3):
    filter = np.random.normal(0, 1, filter_w*filter_h*filter_c).reshape((filter_w, filter_h, filter_c))
    filters.append(filter)


img_out = conv(img, filters, 1)

max_val = np.max(img_out)
min_val = np.min(img_out)

img_out_norm = (img_out - min_val) / (max_val - min_val)

plt.imshow(img_out_norm)
plt.show()