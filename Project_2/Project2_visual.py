import cv2 as cv
import numpy as np

SCALE_FACTOR = 2

BLUE = (255, 0, 0)
DARK_GREEN = (15, 168, 33)
GREEN = (0, 255, 0)

RED = (0, 0, 255)
YELLOW = (9, 227, 212)

# for node breakdown
COST_TO_COME = 0
PARENT_NODE = 1
COORDINATES = 2
# for coordinates
X = 0
Y = 1



def DrawMap():
    # Background
    background_color = [199, 198, 195]
    map = np.zeros((251, 601, 3), np.uint8)
    map[:] = background_color

    # box 1 boundry
    pts = np.array([[95, 0], [155, 0],
                    [155, 105], [95, 105]],
                   np.int32)
    cv.fillPoly(map, [pts], YELLOW)

    # box 1
    pts = np.array([[100, 0], [150, 0],
                    [150, 100], [100, 100]],
                   np.int32)
    cv.fillPoly(map, [pts], BLUE)

    # box 2  boundry
    pts = np.array([[100-5, 150-5], [150+5, 150-5],
                    [150+5, 250], [100-5, 250]],
                   np.int32)
    cv.fillPoly(map, [pts], YELLOW)

    # box 2
    pts = np.array([[100, 150], [150, 150],
                    [150, 250], [100, 250]],
                   np.int32)
    cv.fillPoly(map, [pts], BLUE)

    # hexagon boundry
    pts = np.array([[300, 50-5], [365+4, 87-2], [365+4, 161+2],
                    [300, 200+5], [235-4, 161+2], [235-4, 87-2]],
                   np.int32)
    cv.fillPoly(map, [pts], YELLOW)

    # hexagon
    pts = np.array([[300, 50], [365, 87], [365, 161],
                    [300, 200], [235, 161], [235, 87]],
                   np.int32)
    cv.fillPoly(map, [pts], BLUE)

    # triangle boundry
    pts = np.array([[456, 20], [462, 20], [515, 125], [462, 230], [456, 230]], np.int32)
    cv.fillPoly(map, [pts], YELLOW)

    # triangle
    pts = np.array([[460, 25], [510, 125], [460, 225]], np.int32)
    cv.fillPoly(map, [pts], BLUE)

    return map


def determine_valid_point(coordinates):
    if not point_is_inside_map(coordinates[X], coordinates[Y]):
        return False
    if point_is_inside_box1(coordinates[X], coordinates[Y]):
        return False
    if point_is_inside_box2(coordinates[X], coordinates[Y]):
        return False
    if point_is_inside_hexagon(coordinates[X], coordinates[Y]):
        return False
    if point_is_inside_triangle(coordinates[X], coordinates[Y]):
        return False
    else:
        return True


def point_is_inside_map(x, y):
    if (x > 600) or (x < 0):
        return False
    elif (y > 250) or (y < 0):
        return False
    else:
        return True


def point_is_inside_box1(x, y):
    if (x >= 95) and (x <= 155) and (y >= 0) and (y <= 105):
        return True


def point_is_inside_box2(x, y):
    if (x >= 95) and (x <= 155) and (y >= 145) and (y <= 250):
        return True


def above_line_1(x, y):
    # p1 = (300, 44)  p2 = (370, 85)
    m = (85-44)/(370-300)
    y_line = m * (x - 300) + 44
    if y > y_line:
        return True
    else:
        return False


def below_line_2(x, y):
    # p1=(300, 206)  p2=(370, 164)
    m = (164-206)/(370-300)
    y_line = m * x - m * 300 + 206
    if y < y_line:
        return True
    else:
        return False


def below_line_3(x, y):
    # [300, 206], [230, 163]
    m = (206-163)/(300-230)
    y_line = m * (x - 300) + 206
    if y < y_line:
        return True
    else:
        return False


def above_line_4(x, y):

    # [230, 84], [300, 44]
    m = (44-84)/(300-230)
    y_line = m * (x - 230) + 84
    if y > y_line:
        return True
    else:
        return False


def point_is_inside_hexagon(x, y):
    if above_line_1(x, y) \
    and (x < 370) \
    and below_line_2(x, y) \
    and below_line_3(x, y) \
    and (x > 230) \
    and above_line_4(x, y):
        return True
    else:
        return False


def above_line_5(x, y):
    # [462, 20], [515, 125]
    m = (125 - 20)/(516 - 462)
    y_line = m * (x - 462) + 20
    if y > y_line:
        return True
    else:
        return False


def below_line_6(x, y):
    # [463, 231],  [516, 125]
    m = (125 - 231)/(516 - 463)
    y_line = m * (x - 463) + 231
    if y < y_line:
        return True
    else:
        return False


def point_is_inside_triangle(x, y):
    if (x>455) \
    and (y>19) \
    and above_line_5(x, y) \
    and below_line_6(x, y) \
    and (y<231):
        return True
    else:
        return False


def add_point(x, y, map, color):
    map[y, x] = color
    return map


def run_simulation():
    map = DrawMap()
    # map = cv.resize(src=map, dsize=[600 * SCALE_FACTOR, 250 * SCALE_FACTOR], fx=2, fy=2)
    cv.imshow('Djikstra\'s Algorith', map)
    cv.waitKey(1)
    counter = 1

    for x in range(0, 600):
        for y in range(0, 250):
            valid = determine_valid_point(x, y)
            if valid:
                map[y, x] = DARK_GREEN
            counter += 1
            if counter == 100:
                counter = 0
                cv.imshow('Djikstra\'s Algorith', map)
                cv.waitKey(1)

    cv.imshow('Djikstra\'s Algorith', map)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
   # [235, 87]
    map = DrawMap()
    map = add_point(235, 87, map)
    cv.imshow('Djikstra\'s Algorith', map)
    cv.waitKey(0)

    print(point_is_inside_hexagon(298, 48))
    run_simulation()

    #print(point_is_inside_hexagon(309, 50))
