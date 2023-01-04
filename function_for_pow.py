from math import pow


def wrapper(arg1, arg2):
    if not(isinstance(arg1, (int, float)) and isinstance(arg2, (int, float))):
        msg = "must be int or float, given " + str(type(arg1))
        raise TypeError(msg)
    return pow(float(arg1), float(arg2))


assert(wrapper(2, 3)) == 8.0
