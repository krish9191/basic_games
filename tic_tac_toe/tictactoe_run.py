from tictactoe_manager import is_all_0, is_all_1, is_diagonal_0, is_diagonal_1, create_square_matrix, matrix_transpose
import keyboard


def tic_tac_toe():
    n = int(input('enter the number to create NXN square matrix:'))
    matrix = create_square_matrix(n)
    left_diagonal = []
    right_diagonal = []
    last_value = None
    for entries in range(n * n):
        row, column, value = map(int, input().split())
        if last_value == value:
            if last_value == 0:
                print(" it's 1's turn")
            else:
                print(" it's 0's turn")
        # if keyboard.is_pressed('enter'):
        #     return 'GAME TERMINATED'
        if row + column == len(matrix) - 1:
            right_diagonal.append(value)
        if row == column:
            left_diagonal.append(value)
        matrix[row][column] = value
        last_value = value

        t_matrix = matrix_transpose(matrix)
        if any([is_all_0(matrix), is_diagonal_0(left_diagonal, right_diagonal, n), is_all_0(t_matrix)]):
            print('GAME OVER')
            return 'player 0 is the winner'
        elif any([is_all_1(matrix), is_diagonal_1(left_diagonal, right_diagonal, n), is_all_1(t_matrix)]):
            print('GAME OVER')
            return 'player 1 is the winner'
    return 'this game is draw'


if __name__ == '__main__':
    game = tic_tac_toe()
    print(game)
