import math

import numpy as np


class GameBoard:
    def __init__(self, rows, cols,boardindex):
        self.boardindex = boardindex
        self.rows = rows
        self.cols = cols

        if rows == 2 and cols == 3:
            if self.boardindex==0:
                self.board = [[True, False, False],
                            [True, True, False]]
            elif self.boardindex==1:
                self.board=[[True,False,True],
                            [True,False,True]]
            elif self.boardindex==2:
                self.board=[[False,True,False],
                            [False,True,False]]
            elif self.boardindex==3:
                self.board=[[True,True,True],
                            [True,True,True]]
            elif self.boardindex==4:
                self.board=[[False,True,False],
                            [True,True,True]]




        elif rows==5 and cols==5:
            if self.boardindex == 1:
                self.board = [[True, True, False, True, False],
                              [False, True, False, True, True],
                              [True, True, True, False, False],
                              [True, False, True, False, False],
                              [True, True, False, False, True]]
            elif self.boardindex == 3:
                self.board=[[True,True,True,True,False],
                            [False, False,True, False, True],
                            [False, True,True,True,False],
                            [True,False,True,True,False],
                            [True,True,False,False,True]]

            elif self.boardindex == 2:
                self.board = [[False, True, False, False, False],
                              [False, False, False, True, False],
                              [False, True, True, True, False],
                              [True, False, True, False, False],
                              [False, False, False, True, False]]
            elif self.boardindex == 0:
                self.board=[[False,True,False,False,False],
                            [False, False,False, True, False],
                            [True,True,True,True,True],
                            [True,False,True,False,False],
                            [False,False,False,True,False]]
            elif self.boardindex == 4:
                self.board=[[False,True,False,True,False],
                            [False, False,True, False, True],
                            [True, True,False,True,True],
                            [False,True,False,True,True],
                            [False,True,False,False,True]]
            # elif self.boardindex == 5:
            #     self.board=[[False,True,False,False,True],
            #                 [False, False,True, True, False],
            #                 [True, True,False,False,False],
            #                 [False,True,False,False,False],
            #                 [True,False,False,False,True]]
        # if map_index==0:
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

    def create_same_state(self):
        new_board = GameBoard(self.rows, self.cols,self.boardindex)
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

    # function which returns h() function - heuristic.. in our case its lights that are on
    def get_h(self):

        count = 0
        for row in self.board:
            for light in row:
                if light:
                    count += 1
        return count

    def generate_children(self):
        neighbors = []
        for row in range(self.rows):
            for col in range(self.cols):
                new_state = self.create_same_state()
                new_state.toggle_light(row, col)
                neighbors.append(new_state)
        return neighbors

    def get_child_w_best_h(self, neighbors):
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

    def get_path(self):
        return self.path




