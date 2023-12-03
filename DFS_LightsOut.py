from time import sleep
import heapq
import GameBoard

# class GameBoard:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#
#         # self.board = [[True, True, False, True, True],
#         #             [True, False, False, False, True],
#         #             [False, False, False, False, False],
#         #             [True, False, False, False, True],
#         #             [True, True, False, True, True]]
#
#         # self.board = [[True, False, False,False],
#         #                 [True, True, False, True],
#         #                 [False, True, True,False]]
#
#         self.board = [[True, True, False, True],
#                         [True, False, False, False]]
#
#
#     def toggle_light(self, row, col):
#         self.board[row][col] = not self.board[row][col]
#         if row > 0:
#             self.board[row - 1][col] = not self.board[row - 1][col]
#         # toggle the light below, if it exists
#         if row < self.rows - 1:
#             self.board[row + 1][col] = not self.board[row + 1][col]
#         # toggle the light to the left, if it exists
#         if col > 0:
#             self.board[row][col - 1] = not self.board[row][col - 1]
#         # toggle the light to the right, if it exists
#         if col < self.cols - 1:
#             self.board[row][col + 1] = not self.board[row][col + 1]
#
#     def __str__(self):
#         result = ""
#         for row in self.board:
#             for light in row:
#                 result += "*" if light else "."
#             result += "\n"
#         return result
#
#     def is_solved(self):
#         for row in self.board:
#             for light in row:
#                 if light:
#                     return False
#         return True
#
#     def copy(self):
#         new_board = GameBoard(self.rows, self.cols)
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 new_board.board[row][col] = self.board[row][col]
#         return new_board
#
#     #create a function to check if the state is in the visited set
#     def is_in_visited(self, visited):
#         # convert the state to a tuple
#         state_tuple = tuple(map(tuple, self.board))
#         # check if the state tuple is in the visited set
#         if state_tuple in visited:
#             return True
#         else:
#             return False



class LightsOutSolver_DFS:
    def __init__(self, board):
        self.board = board
        self.moves = []
        self.solved = False

    #

    def solve_dfs(self):
        # create a stack to store the states to be expanded
        stack = []
        # create a set to store the states that have been visited
        visited = set()
        # create a dictionary to store the predecessors of each state
        predecessors = {}
        # push the initial state to the stack
        stack.append(self.board)
        visited.add(self.board)
        predecessors[self.board] = None

        
        index_of_while=0
        # while the stack is not empty
        while stack:
            # sleep(1)
            index_of_while+=1
            # pop a state from the stack
            current_state = stack.pop()
            visited.add(tuple(map(tuple, current_state.board)))
            # print("popped from stack")
            # print(current_state)
            if current_state.is_solved():
                # set the solved flag to True
                self.solved = True
                # set the moves list to the empty list
                self.moves = []
                self.moves.append(current_state)
                # set the current state to the predecessor of the current state
                while predecessors[current_state] is not None:
                    # append the move that was made to get to the current state to the moves list
                    self.moves.append(predecessors[current_state])
                    # set the current state to the predecessor of the current state
                    current_state = predecessors[current_state]
                # reverse the moves list

                self.moves.reverse()
                # break out of the loop
                break
            # for each possible move
            for row in range(self.board.rows):
                for col in range(self.board.cols):
                    # create a copy of the current state
                    new_state = current_state.copy()
                    # make the move on the copy
                    new_state.toggle_light(row, col)
                    #print("new state")
                    #print(new_state)
                    # if the copy has not been visited
                    if new_state.is_in_visited(visited) is False:
                        # print("if new_state not in visited:")
                        # print(new_state)
                        # push the copy to the stack
                        stack.append(new_state)
                        # add the copy to the visited set
                        visited.add(tuple(map(tuple, new_state.board)))
                        # set the predecessor of the copy to the current state
                        predecessors[new_state] = current_state

    def get_moves(self):
        return self.moves

    def get_num_moves(self):
        return len(self.moves)

    def get_num_states(self):
        return len(self.moves) + 1

    # def get_states(self):
    #     states = []
    #     current_state = self.board
    #     states.append(current_state)
    #     for move in self.moves:
    #         current_state = current_state.copy()
    #         current_state.toggle_light(move[0], move[1])
    #         states.append(current_state)
    #     return states











# Testing the GameBoard class
if __name__ == "__main__":
    # Create an instance of the GameBoard class
    initial_board = GameBoard.GameBoard(2, 4)

    # Print the initial state of the board
    print("Initial State:")
    print(initial_board)


    solver = LightsOutSolver_DFS(initial_board)
    solver.solve_dfs()
    print("Moves:")
    moves= solver.get_moves()
    for move in moves:
        print(move)

    print("Number of moves:", solver.get_num_moves())
    print("Number of states:", solver.get_num_states())
    print(solver.solved)


    # solver.solve_a_star()
    # print("Moves:")
    # moves= solver.get_moves()
    # for move in moves:
    #     print(move)
    # print("Number of moves:", solver.get_num_moves())
    # print("Number of states:", solver.get_num_states())





