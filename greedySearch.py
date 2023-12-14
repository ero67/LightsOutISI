import GameBoard
import heapq
import time




class greedySearchSolver:
    def __init__(self, board):
        self.board = board
        self.moves = []
        self.solved = False
        self.closedList = set()
        self.time = 0
    def solve_greedy(self):
        priority_queue = []
        initial_state = self.board

        #pushing inital state with its heuristic to priority queue
        heapq.heappush(priority_queue, (initial_state.get_h(), initial_state))
        # moves = []
        # closedList = set()
        self.closedList.add(initial_state)
        parrents = {}
        parrents[initial_state] = None
        start_time = time.time()

        while len(priority_queue) > 0:
            # poping the state with the lowest h from the priority queue with index 1 of a tuple bacause the first element is the h
            current_state = heapq.heappop(priority_queue)[1]
            print("current state")
            print(current_state)

            if current_state.is_solved():
                self.solved = True
                self.moves = []
                self.moves.append(current_state)
                while parrents[current_state] is not None:
                #     # append the move that was made to get to the current state to the moves list
                     self.moves.append(parrents[current_state])
                #     # set the current state to the parrent of the current state
                     current_state = parrents[current_state]
                # reverse the moves list
                self.moves.reverse()

                #get the final time of running the algorithm
                self.time = time.time() - start_time
                break
            children = current_state.generate_children()
            for child in children:
                # print("child")
                # print(child)
                if child not in self.closedList:
                    # print("child not in closed list")
                    # print(child)
                    heapq.heappush(priority_queue, (child.get_h(), child))
                    self.closedList.add(child)
                    parrents[child] = current_state

            # time.sleep(3)
    def get_moves(self):
        return self.moves

    def get_num_moves(self):
        return len(self.moves)-1

    def get_num_expanded_states(self):
        return len(self.closedList)
    def get_time(self):
        return self.time

if __name__ == "__main__":
    initial_state = GameBoard.GameBoard(2, 3,4)
    # print(initial_state)
    # create a solver object
    solver = greedySearchSolver(initial_state)
    solver.solve_greedy()
    moves = solver.get_moves()

    print("Greedy")
    print("Number of expanded states:")
    print(solver.get_num_expanded_states())
    print("Number of moves:")
    print(solver.get_num_moves())
    print(solver.solved)
    print("Time:")
    print(solver.get_time())







