import math

import numpy as np


class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        # self.board = [[True, True, False, True, True],
        #             [True, False, False, False, True],
        #             [False, False, False, False, False],
        #             [True, False, False, False, True],
        #             [True, True, False, True, True]]

        # self.board = [[True, False, False,False],
        #                 [True, True, False, True],
        #                 [False, True, True,False]]

        # self.board = [[True, True, False, True],
        #                 [True, False, True, True]]

        # self.board = [[True, False, False, True],
        #               [False, True, True, False],
        #               [True, False, False, True]]

        # self.board = [[False, False, False, False],
        #               [False, False, False, False]]

        # self.board=[[False,True,False,False,False],
        #             [False, False,False, True, False],
        #             [False, True,True,True,False],
        #             [True,False,True,False,False],
        #             [False,False,False,True,False]]

        self.board=[[True,True,True],
                    [True,True,True],
                    [False,False,False]]
        # path to the current state.... for a* algo
        self.path = []





    def toggle_light(self, row, col):
        self.board[row][col] = not self.board[row][col]
        if row > 0:
            self.board[row - 1][col] = not self.board[row - 1][col]
        # toggle the light below, if it exists
        if row < self.rows - 1:
            self.board[row + 1][col] = not self.board[row + 1][col]
        # toggle the light to the left, if it exists
        if col > 0:
            self.board[row][col - 1] = not self.board[row][col - 1]
        # toggle the light to the right, if it exists
        if col < self.cols - 1:
            self.board[row][col + 1] = not self.board[row][col + 1]

        #add tuple of row and col to the path list
        self.path.append((row, col))


    def __str__(self):
        result = ""
        for row in self.board:
            for light in row:
                result += "*" if light else "."
            result += "\n"
        return result

    def is_solved(self):
        for row in self.board:
            for light in row:
                if light:
                    return False
        return True

    def copy(self):
        new_board = GameBoard(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                new_board.board[row][col] = self.board[row][col]
        return new_board

    #create a function to check if the state is in the visited set
    def is_in_visited(self, visited):
        # convert the state to a tuple
        state_tuple = tuple(map(tuple, self.board))
        # check if the state tuple is in the visited set
        if state_tuple in visited:
            return True
        else:
            return False

    # function which returns h() function - heuristic
    def get_h(self):
        # return the number of lights that are on
        count = 0
        for row in self.board:
            for light in row:
                if light:
                    count += 1
        return count

    def get_neighbors(self):
        neighbors = []
        for row in range(self.rows):
            for col in range(self.cols):
                new_state = self.copy()
                new_state.toggle_light(row, col)
                neighbors.append(new_state)
        return neighbors

    def get_best_neighbor(self,neighbors):
        # neighbors = self.get_neighbors()
        best_neighbor = neighbors[0]
        for neighbor in neighbors:
            if neighbor.get_h() < best_neighbor.get_h():
                best_neighbor = neighbor
        return best_neighbor
    def get_last_move(self):
        return self.path[-1]

    def get_g(self):
        return len(self.path)

    def get_f(self):
        return self.get_h() + self.get_g()

    def __lt__(self, other):
        return self.get_h() < other.get_h()

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    # def __eq__(self, other):
    #     # check if the other object is a GameBoard
    #     if isinstance(other, GameBoard):
    #         # compare the board matrices of the two objects
    #         return np.array_equal(self.board, other.board)
    #     else:
    #         # return False if the other object is not a GameBoard
    #         return False

    # def __hash__(self):
    #     # convert the board matrix to a string
    #     board_string = str(self.board)
    #     # return the hash value of the string
    #     return hash(board_string)



