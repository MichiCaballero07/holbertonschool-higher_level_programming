def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_matrix = [list(map(lambda num: num ** 2, i)) for i in matrix]
    return new_matrix
