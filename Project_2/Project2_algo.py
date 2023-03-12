from queue import PriorityQueue
from Project2_visual import determine_valid_point

COST_TO_COME = 0
PARENT_NODE = 1
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


def backtrack(end_node):
    print("done")
    exit()


def generate_graph():
    rows = 250
    cols = 600
    graph = [[float('infinity') for _ in range(rows)] for _ in range(cols)]
    for x in range(cols):
        for y in range(rows):
            if not determine_valid_point((x, y)):
                graph[x][y] = -1
    return graph


def check_open_list(node):
    for i in range(open_list.qsize()):
        DEBUG_open_node = open_list.queue[i]
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
    closed_list = set()  # stores just visited locations

    starting_node = (0, None, (0, 0))
    goal_coordinates = (125, 110)

    open_list.put(starting_node)
    current_node = open_list.get()

    while current_node[COORDINATES] != goal_coordinates:
    #for i in range(10):
        closed_list.add(current_node[COORDINATES])

        # get neighbors
        # neighbors are already checked to see if they are valid
        neighbor_nodes = get_neighbor_nodes(current_node)

        for node in neighbor_nodes:
            if node[COORDINATES] in closed_list:
                continue
            else:
                check_open_list(node)

        # iteration done. get the node with the lowest cost to come
        current_node = open_list.get()

    backtrack(1)
