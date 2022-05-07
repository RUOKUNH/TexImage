import numpy as np
import cv2
import pdb

def extract(img):
# img = cv2.imread("test_images/cat3.jpg", 0)
    blurred = cv2.GaussianBlur(img,(11,11),0)
    edge = cv2.Canny(blurred, 10, 50)
    # cv2.imshow("Img",edge)
    # cv2.waitKey(0)
    return edge

def judge_line_type(block):
    if not np.any(block > 0):
        return ' '
    edge_point = np.argwhere(block == 255)
    point_cnt = edge_point.shape[0]
    mx, my = np.mean(edge_point, axis=0)
    x_score = np.sum(edge_point[:, 0]**2) - point_cnt * mx**2
    y_score = np.sum(edge_point[:, 1]**2) - point_cnt * my**2
    return '|' if y_score < x_score else '-'
