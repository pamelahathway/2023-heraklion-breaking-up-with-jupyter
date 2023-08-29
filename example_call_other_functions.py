from example1_namespace import increase_by_one


def divide_by_3(a):
    intermediate_result = increase_by_one(a)
    return intermediate_result/3


def get_calculation_result(n1, n2):
    return divide_by_3(n1) - divide_by_3(n2)


