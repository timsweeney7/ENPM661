import cv2 as cv
import numpy as np

SCALE_FACTOR = 2


def DrawMap():
    # Background
    background_color = [199, 198, 195]
    map = np.zeros((250, 600, 3), np.uint8)
    map[:] = background_color

    # box 1
    pts = np.array([[100, 0], [150, 0],
                    [150, 100], [100, 100]],
                   np.int32)
    color = (255, 0, 0)
    box1 = cv.fillPoly(map, [pts], color)

    # box 2
    pts = np.array([[100, 150], [150, 150],
                    [150, 250], [100, 250]],
                   np.int32)
    color = (255, 0, 0)
    box1 = cv.fillPoly(map, [pts], color)

    # hexagon
    pts = np.array([[300, 50], [365, 87], [365, 161],
                    [300, 200], [335, 161], [335, 87]],
                   np.int32)
    hexagon = cv.fillPoly(map, [pts], color)

    # triangle
    pts = np.array([[460, 25], [510, 125], [460, 225]], np.int32)
    triangle = cv.fillPoly(map, [pts], color)


    map = cv.resize(src=map, dsize=[600*SCALE_FACTOR, 250*SCALE_FACTOR], fx=2, fy=2)
    cv.imshow('Djikstra\'s Algorith', map)
    cv.waitKey(0)
    cv.destroyAllWindows()


def determine_valid_point(x, y):
    if not point_is_inside_map(x, y):
        return False
    if point_is_inside_box1(x, y):
        return False
    print()


def point_is_inside_map(x, y):
    if (x>600) or (x<0):
        return False
    elif (y>250) or (y<0):
        return False
    else:
        return True


def point_is_inside_box1(x, y):
    if (x > 100) and (x < 150) and (y > 0) and (y < 100):
        return True

"""    
def point_is_inside_box2(x, y):
    if (x > 100) and (x < 150) and (y > ) and ()
"""