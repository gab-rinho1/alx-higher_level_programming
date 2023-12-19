#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
    my_list(list): Thte list to print elements from.
    x (int): The number of elements of m_list to print.

    Returns:
        The number of elements printed.
    """
    gap = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            gap +=1
        except IndexError:
            break
        print("")
        return(gap)
