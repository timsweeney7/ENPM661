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
                (old_node[COORDINATES][X] - 1, old_node[COORDINATES][X] - 1)  # child coordinates (x, y)
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


if __name__ == "__main__":

    # (c2c, parent_node, (x, y))
    open_list = PriorityQueue()
    closed_list = {}
    start_node = (0, None, (0, 0))
    current_node = (0, None, (330, 125))
    goal_state = (550, 245)
    open_list.put(start_node)
    current_node = open_list.get()

    print(get_neighbor_nodes(current_node))

