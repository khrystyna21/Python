# task 6
from enum import Enum


class SortOrder(Enum):
    ASC = 'ASC'
    DESC = 'DESC'


def IsSorted(array, order):
    flag = 0
    i = 1
    while i < len(array):
        if (array[i] < array[i - 1]) and order == SortOrder.ASC.value:
            flag = 1
        if (array[i] > array[i - 1]) and order == SortOrder.DESC.value:
            flag = 1
        i +=1
    if not flag:
        return True
    else:
        return False


arr = [8, 7, 1]
print(IsSorted(arr, 'DESC'))

arr = [1, 4, 5]
print(IsSorted(arr, 'ASC'))





