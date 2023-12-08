import GameBoard
import heapq
import time

class greedySearchSolver:
    def __init__(self, board):
        self.board = board
        self.moves = []
        self.solved = False
        self.closedList = set()
    def solve_greedy(self):
        priority_queue = []
        initial_state = self.board
        heapq.heappush(priority_queue, (initial_state.get_h(), initial_state))
        # second_state=initial_state.copy()
        # second_state.toggle_light(0,0)
        # third_state=second_state.copy()
        # third_state.toggle_light(2,2)
        # heapq.heappush(priority_queue, (second_state.get_h(), second_state))
        # heapq.heappush(priority_queue, (third_state.get_h(), third_state))
        #
        # popped= heapq.heappop(priority_queue)[1]
        # print(popped)
        # popped = heapq.heappop(priority_queue)[1]
        # print(popped)
        # popped = heapq.heappop(priority_queue)[1]
        # print(popped)
        moves = []
        # closedList = set()
        self.closedList.add(initial_state)
        predecessors = {}
        predecessors[initial_state] = None

        while len(priority_queue) > 0:
            # poping the state with the lowest h from the priority queue with index 1 of a tuple bacause the first element is the h
            current_state = heapq.heappop(priority_queue)[1]
            # print("this is priority queue")
            # for item in priority_queue:
            #     print(item)
            # print("this is end of priority queue")
            # print("this is closed list")
            # for item in closedList:
            #     print(item)
            # print("this is end if the closed list")
            # print("state with the lowest h in the queue")
            # print(current_state)
            if current_state.is_solved():
                self.solved = True
                self.moves = []
                self.moves.append(current_state)
                # # set the current state to the predecessor of the current state
                # print(current_state)
                while predecessors[current_state] is not None:
                #     # append the move that was made to get to the current state to the moves list
                     self.moves.append(predecessors[current_state])
                #     # set the current state to the predecessor of the current state
                     current_state = predecessors[current_state]
                # # reverse the moves list
                #
                self.moves.reverse()
                # break out of the loop
                # print("solved")
                # print(current_state)
                print(current_state.get_path())
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
                    predecessors[child] = current_state

            # time.sleep(3)
    def get_moves(self):
        return self.moves

    def get_num_moves(self):
        return len(self.moves)

    def get_num_expanded_states(self):
        return len(self.closedList)


if __name__ == "__main__":
    initial_state = GameBoard.GameBoard(5, 5,1)
    # print(initial_state)
    # create a solver object
    solver = greedySearchSolver(initial_state)
    solver.solve_greedy()
    moves = solver.get_moves()
    print("Number of expanded states:")
    print(solver.get_num_expanded_states())





