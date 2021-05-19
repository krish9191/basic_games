def create_square_matrix(number):
    return [[8 for i in range(number)] for j in range(number)]


def matrix_transpose(arr):
    arr_t = [[8 for i in range(len(arr))] for j in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr_t[j][i] = arr[i][j]
    return arr_t


def is_all_0(arr):
    for row in arr:
        if sum(row) == 0:
            return True


def is_all_1(arr):
    for row in arr:
        if sum(row) == len(arr):
            return True


def is_diagonal_0(left_diagonal, right_diagonal, number_of_square_matrix):
    if (len(left_diagonal) == number_of_square_matrix and sum(left_diagonal) == 0) or (
            len(right_diagonal) == number_of_square_matrix and sum(right_diagonal) == 0):
        return True


def is_diagonal_1(left_diagonal, right_diagonal, number_of_square_matrix):
    if (len(left_diagonal) == number_of_square_matrix and sum(left_diagonal) == number_of_square_matrix) or (
            len(right_diagonal) == number_of_square_matrix and sum(right_diagonal) == number_of_square_matrix):
        return True
