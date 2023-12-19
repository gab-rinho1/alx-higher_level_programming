#!/usr/bin/python3

def safe_print_integer(value):
    """Print an interger with "{:d}".format().

    Args:
        value (int): the interger to print.

    Returns:
        if a TypeError or ValueError occurs - False.
        otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return(True)
    except(TypeError, ValueError):
        return(False)

