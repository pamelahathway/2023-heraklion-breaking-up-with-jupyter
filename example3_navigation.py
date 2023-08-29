import numpy as np

from example2_debug import create_figure
from example_call_other_functions import get_calculation_result


def run():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([7, 3, 1])
    result1 = get_calculation_result(arr1, arr2)

    arr3 = np.array([4, 7, 1])
    arr4 = np.array([0, 2, 9])
    result2 = get_calculation_result(arr3, arr4)

    create_figure(result1, result2, "this is just a demo")


if __name__ == "__main__":
    run()