"""Array allocation functions"""

import math

#Right-shifted
def mode_allocator(modes,cores):

    """Given a number of AVR task modes and a number of cores, divide the modes among the cores"""

    sub_arrays = []*cores
    sub_array_size_min = math.floor(modes/cores)
    sub_array_size_max = sub_array_size_min+1
    last_n_are_larger = modes%cores
    first_larger_index = cores-last_n_are_larger

    mode_current = 1
    size_current = sub_array_size_min

    for i in range(cores):

        appended = 0
        to_add = []

        if i >= first_larger_index:
            size_current = sub_array_size_max

        while appended < size_current:
            to_add.append(mode_current)
            appended+=1
            mode_current+=1

        sub_arrays.append(to_add)

    return sub_arrays

##Round robin
def delta_allocator(deltas,cores):

    """Given num of array elements (deltas), divide the elements into n-separate bins (cores)"""

    sub_arrays = [-1]*cores
    for i in range(cores):
        sub_arrays[i] = deltas[i::cores]

    return sub_arrays

##Round robin, starts at zero
def node_allocator(num_nodes,cores):

    """Given num of array elements (deltas), divide the elements into n-separate bins (cores)"""

    sub_arrays = [-1]*cores
    for i in range(cores):
        sub_arrays[i] = list(range(num_nodes))[i::cores]

    return sub_arrays
