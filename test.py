import re


def comp(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return False


    array1.sort()
    array2.sort()

    for i, elt in enumerate(array1):
        if (elt * elt) != array2[i]:
            return False

    return True


if __name__ == '__main__':
    a = [3, 6, 7, 3, 6, 4, 2]
    b = [6241]

    print(comp(a, b))
