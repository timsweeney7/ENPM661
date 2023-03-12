from queue import PriorityQueue
from Project2_visual import *
import cv2 as cv

COST_TO_COME = 0
PARENT_COORDINATES = 1
COORDINATES = 2

# for coordinates
X = 0
Y = 1


def action_move_north(old_node):
    new_node = (old_node[COST_TO_COME] + 1,  # cost to come
                old_node[COORDINATES],       # parent index
                (old_node[COORDINATES][X], old_node[COORDINATES][Y]+1)   # child coordinates (x, y)
                )
    return new_node


def action_move_south(old_node):
    new_node = (old_node[COST_TO_COME] + 1,  # cost to come
                old_node[COORDINATES],       # parent index
                (old_node[COORDINATES][X], old_node[COORDINATES][Y]-1)   # child coordinates (x, y)
                )
    return new_node


def action_move_east(old_node):
    new_node = (old_node[COST_TO_COME] + 1,  # cost to come
                old_node[COORDINATES],  # parent index
                (old_node[COORDINATES][X]+1, old_node[COORDINATES][Y])  # child coordinates (x, y)
                )
    return new_node


def action_move_west(old_node):
    new_node = (old_node[COST_TO_COME] + 1,  # cost to come
                old_node[COORDINATES],  # parent index
                (old_node[COORDINATES][X]-1, old_node[COORDINATES][Y])  # child coordinates (x, y)
                )
    return new_node


def action_move_north_east(old_node):
    new_node = (old_node[COST_TO_COME] + 1.4,  # cost to come
                old_node[COORDINATES],  # parent index
                (old_node[COORDINATES][X]+1, old_node[COORDINATES][Y]+1)  # child coordinates (x, y)
                )
    return new_node


def action_move_south_east(old_node):
    new_node = (old_node[COST_TO_COME] + 1.4,  # cost to come
                old_node[COORDINATES],  # parent index
                (old_node[COORDINATES][X] + 1, old_node[COORDINATES][Y] - 1)  # child coordinates (x, y)
                )
    return new_node


def action_move_south_west(old_node):
    new_node = (old_node[COST_TO_COME] + 1.4,  # cost to come
                old_node[COORDINATES],  # parent index
                (old_node[COORDINATES][X] - 1, old_node[COORDINATES][Y] - 1)  # child coordinates (x, y)
                )
    return new_node


def action_move_north_west(old_node):
    new_node = (old_node[COST_TO_COME] + 1.4,  # cost to come
                old_node[COORDINATES],  # parent index
                (old_node[COORDINATES][X] - 1, old_node[COORDINATES][Y] + 1)  # child coordinates (x, y)
                )
    return new_node


def get_neighbor_nodes(node):
    valid_neighbors = []

    new_node = action_move_north(node)   # north
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    new_node = action_move_south(node)   # south
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    new_node = action_move_east(node)   # east
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    new_node = action_move_west(node)   # west
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    new_node = action_move_north_east(node)  # north_east
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    new_node = action_move_north_west(node)  # north_west
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    new_node = action_move_south_east(node)  # south east
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    new_node = action_move_south_west(node)  # south west
    if determine_valid_point(new_node[COORDINATES]):
        valid_neighbors.append(new_node)

    return valid_neighbors


def backtrack(last_node):
    print('Backtracking!')
    solution_list = []
    solution_list.append(last_node[COORDINATES])
    current_node = last_node
    while current_node[PARENT_COORDINATES] is not None:
        solution_list.append(current_node[PARENT_COORDINATES])
        current_node = graph [current_node[PARENT_COORDINATES][X]] [current_node[PARENT_COORDINATES][Y]]

    solution_list.reverse()
    return solution_list


def generate_graph():
    rows = 251
    cols = 601
    graph = [[0 for _ in range(rows)] for _ in range(cols)]
    for x in range(cols):
        for y in range(rows):
            if not determine_valid_point((x, y)):
                graph[x][y] = -1
    return graph


def check_open_list(node):
    for i in range(open_list.qsize()):
        if open_list.queue[i][COORDINATES] == node[COORDINATES]:
            if node[COST_TO_COME] < open_list.queue[i][COST_TO_COME]:
                open_list.queue[i] = node
                return
            else:
                return
    # node is not in the open list
    open_list.put(node)



if __name__ == "__main__":
    open_list = PriorityQueue()  # stores node distance, parent, and location
    closed_list_set = set()  # stores just visited locations
    closed_list_array = []
    graph = generate_graph()

    starting_node = (0, None, (0, 0))
    goal_coordinates = (600, 250)

    open_list.put(starting_node)
    current_node = open_list.get()
    graph [current_node[COORDINATES][X]] [current_node[COORDINATES][Y]] = \
        (current_node[COST_TO_COME], current_node[PARENT_COORDINATES])

    while current_node[COORDINATES] != goal_coordinates:
        closed_list_set.add(current_node[COORDINATES])
        closed_list_array.append(current_node[COORDINATES])
        graph[current_node[COORDINATES][X]][current_node[COORDINATES][Y]] = \
            (current_node[COST_TO_COME], current_node[PARENT_COORDINATES])

        # get neighbors
        # neighbors are already checked to see if they are valid
        neighbor_nodes = get_neighbor_nodes(current_node)

        for node in neighbor_nodes:
            if node[COORDINATES] in closed_list_set:
                continue
            else:
                check_open_list(node)

        # iteration done. get the node with the lowest cost to come
        current_node = open_list.get()

    # done traversing graph
    closed_list_set.add(current_node[COORDINATES])
    closed_list_array.append(current_node[COORDINATES])
    graph[current_node[COORDINATES][X]][current_node[COORDINATES][Y]] = \
        (current_node[COST_TO_COME], current_node[PARENT_COORDINATES])

    solution = backtrack(current_node)
    print(solution)

    map = DrawMap()
    cv.imshow('Djikstra\'s Algorith', map)
    cv.waitKey(1)
    counter = 0

    for node in closed_list_array:
        add_point(node[X], node[Y], map, GREEN)
        counter += 1
        if counter == 50:
            cv.imshow('Djikstra\'s Algorith', map)
            cv.waitKey(1)
            counter = 0

    counter = 0
    for node in solution:
        add_point(node[X], node[Y], map, RED)
        counter += 1
        if counter == 50:
            cv.imshow('Djikstra\'s Algorith', map)
            cv.waitKey(1)
            counter = 0

    cv.waitKey(0)