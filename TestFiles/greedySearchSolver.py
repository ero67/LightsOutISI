import GameBoard
import heapq
import time

class greedySearchSolver:
    def __init__(self, board):
        self.board = board
        self.moves = []
        self.solved = False

    def solve_greedy(self):
        # createing priority queue ... contains tuples (h,state)
        openedList = []

        # add the initial state to the priority queue...(heuristicvalue, board)
        heapq.heappush(openedList, (self.board.get_h(), self.board))

        # create a set to store the states we have already seen
        closedList=set()

        # add the initial state to the set
        closedList.add(self.board)

        predecessors = {}
        # add the initial state to the dictionary
        predecessors[self.board] = None

        # loop until the priority queue is empty
        while len(openedList) > 0:
            # heappop returns a item from queue with lowest h() value
            current_board = heapq.heappop(openedList)[1]
            # print("1 iteration of current board")
            # print(current_board)
            # time.sleep(5)
            if current_board.is_solved():
                self.solved = True
                self.moves = []
                self.moves.append(current_board)
                # set the current state to the predecessor of the current state
                # print(current_board)
                while predecessors[current_board] is not None:
                    # append the move that was made to get to the current state to the moves list
                    self.moves.append(predecessors[current_board])
                    # set the current state to the predecessor of the current state
                    current_board = predecessors[current_board]
                # reverse the moves list

                self.moves.reverse()
                return current_board.path
                # break out of the loop
                break

            # get all the neighbors...that means all the child states possible from sthis state
            neighbors = current_board.generate_children()

            for neighbor in neighbors:
                # check if we have already seen this state
                if neighbor not in closedList:
                    # if not, add it to the priority queue
                    heapq.heappush(openedList, (neighbor.get_h(), neighbor))
                    # add it to the set
                    closedList.add(neighbor)
                    # add the move to the dictionary
                    predecessors[neighbor] = current_board

            # best_neighbor=current_board.get_best_neighbor(neighbors)
            # if best_neighbor not  in closedList:
            #     continue
            # else:
            #     heapq.heappush(openedList, (best_neighbor.get_h(), best_neighbor))
            #     closedList.add(best_nei ghbor)
            #     predecessors[best_neighbor] = current_board
            #     print("best neighbor")
            #     print(best_neighbor)

        return None

    def get_moves(self):
        return self.moves

    def get_num_moves(self):
        return len(self.moves)

if __name__ == "__main__":
    initial_state = GameBoard.GameBoard(3, 3,0)
    # print(initial_state)
    # create a solver object
    solver = greedySearchSolver(initial_state)
    path=solver.solve_greedy()
    for click in path:
        print(click)

    moves= solver.get_moves()

    # for move in moves:
    #     print(move)


