import GameBoard
import time
class LightsOutSolver_DFS:
    def __init__(self, board):
        self.board = board
        self.moves = []
        self.solved = False
        self.num_expaned_states=0
        self.visited=set()
        self.time=0

    def solve_dfs(self):
        start_time = time.time()
        stack = []
        parrents = {}

        # initializing stack, visted and parrents with inital state
        stack.append(self.board)
        self.visited.add(self.board)
        parrents[self.board] = None

        
        index_of_while=0

        while stack:
            # sleep(1)
            index_of_while+=1
            # pop a state from the stack
            current_state = stack.pop()
            print(current_state)
            self.visited.add(tuple(map(tuple, current_state.board)))
            # print("popped from stack")
            # print(current_state)
            if current_state.is_solved():
                self.solved = True
                self.moves.append(current_state)
                print(current_state)
                while parrents[current_state] is not None:
                    # append the move that was made to get to the current state to the moves list
                    self.moves.append(parrents[current_state])
                    # set the current state to the predecessor of the current state
                    current_state = parrents[current_state]

                self.moves.reverse()
                self.time = time.time() - start_time
                break
            # for each possible move
            for row in range(self.board.rows):
                for col in range(self.board.cols):
                    # create a copy of the current state
                    new_state = current_state.create_same_state()
                    # make the move on the copy
                    new_state.toggle_light(row, col)
                    # if the copy has not been visited, i had to create this method for checking if the state is in visited
                    #because it was not working with "not in"
                    if new_state.is_in_visited(self.visited) is False:
                        # push the copy to the stack
                        stack.append(new_state)
                        # add the copy to the visited set ... using tuple because i could not check if the board was already in the set
                        self.visited.add(tuple(map(tuple, new_state.board)))
                        # set the parrent of the copy to the current state
                        parrents[new_state] = current_state

    def get_moves(self):
        return self.moves

    def get_num_moves(self):
        return len(self.moves)-1

    # def get_num_states(self):
    #     return len(self.moves) + 1
    def get_num_expanded_states(self):
        return len(self.visited)

    def get_time(self):
        return self.time









# Testing the GameBoard class
if __name__ == "__main__":
    # Create an instance of the GameBoard class
    initial_board = GameBoard.GameBoard(2, 3,4)

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
    print("Number of expanded states:", solver.get_num_expanded_states())
    print(solver.solved)
    print("Time:")
    print(solver.get_time())







