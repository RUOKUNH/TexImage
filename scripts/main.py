import cv2
from matplotlib.pyplot import text
import numpy as np
from tool_funcs import *
import json
from math import ceil
import os

x_buffer = 150
config = json.load(open('config.json', 'r'))

def main(img_path):
    img = cv2.imread(img_path, 0)
    edge = extract(img)
    H, L = edge.shape
    block_size = ceil(L / x_buffer)
    result = ''
    for i in range(H//block_size):
        for j in range(L//block_size):
            block = edge[block_size*i: block_size*(i+1), block_size*j: block_size*(j+1)]
            result += judge_line_type(block)
        result += '\n'
    print(result)

main('test_images/cat3.jpg')



