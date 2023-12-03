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

        self.board = [[True, True, False, True],
                        [True, False, False, False]]


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