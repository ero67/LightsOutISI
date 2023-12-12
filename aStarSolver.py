import GameBoard
from queue import PriorityQueue
import heapq
from collections import defaultdict
import math

class LightsOutSolver_AStar:

    def __init__(self, board):
        self.board = board
        self.moves = []
        self.solved = False

    # function which takes open list as parameter and returns the node with the lowest f value
    # def lowest_f(self, openList):
    #     lowest_f= openList[0]
    #     for node in openList:
    #         f=node.get_f()
    #         if f<lowest_f.get_f():
    #             lowest_f=node
    #     return lowest_f

    # def lowest_f(self,openList):
    #     # set the lowest_f to the first tuple in the list
    #     lowest_f = openList[0]
    #     # for each tuple in the list
    #     for node in openList:
    #         # get the f value from the first element of the tuple
    #         f = node[0]
    #         # if the f value is lower than the lowest_f value
    #         if f < lowest_f[0]:
    #             # set the lowest_f to the current tuple
    #             lowest_f = node
    #     # return the state from the third element of the lowest_f tuple
    #     return lowest_f[2]

    def get_actions(self, state):
        # create an empty list to store the actions
        actions = []
        # loop through the rows and columns of the board
        for row in range(state.rows):
            for col in range(state.cols):
                # append the coordinates of the light to the actions list
                actions.append((row, col))
        # return the actions list
        return actions

    def apply_action(self, state, action):
        # copy the state to avoid modifying the original
        new_state = state.create_same_state()
        # get the row and column from the action
        row, col = action
        # toggle the light and its neighbors using the toggle_light method
        new_state.toggle_light(row, col)
        # return the new state
        return new_state

    def a_star(self):

        # create an empty list to store the open list
        open_list = []
        # create an empty dictionary to store the parent state and action for each state
        parent_map = {}

        




    # def a_star(self):
    #     # create an empty set to store the visited states
    #     visited = set()
    #     # create an empty list to store the open list
    #     open_list = []
    #     # create an empty dictionary to store the parent state and action for each state
    #     parent_map = {}
    #     # create a defaultdict that returns infinity by default to store the f value for each state
    #     f_map = defaultdict(lambda: math.inf)
    #
    #     # get the initial state from the board attribute
    #     initial_state = self.board
    #     # get the f value of the initial state
    #     initial_f = initial_state.get_f()
    #     # insert the initial state into the open list as a tuple of (f, h, state)
    #     heapq.heappush(open_list, (initial_f, initial_state.get_h(), initial_state))
    #     # set the parent of the initial state to None
    #     parent_map[initial_state] = None
    #     # set the f value of the initial state
    #     f_map[initial_state] = initial_f
    #
    #     # while the open list is not empty
    #     while open_list:
    #         # get the state with the lowest f value from the open list
    #         current_state = heapq.heappop(open_list)[2]
    #         # if the current state is the goal state
    #         print(current_state)
    #         if current_state.is_solved():
    #             # create an empty list to store the solution path
    #             path = []
    #             # set the state to the current state
    #             state = current_state
    #             # while the state is not None
    #             while state is not None:
    #                 # prepend the state to the path list
    #                 path.insert(0, state)
    #                 # get the parent state from the parent map
    #                 state = parent_map[state]
    #             # return the path and the number of moves
    #             return path, len(path) - 1
    #         # add the current state to the visited set
    #         visited.add(tuple(map(tuple, current_state.board)))
    #         # get the possible actions from the current state
    #         actions = self.get_actions(current_state)
    #         # for each action
    #         for action in actions:
    #             # apply the action to the current state and get the next state
    #             next_state = self.apply_action(current_state, action)
    #             print(next_state)
    #             # if the next state is not in the visited set
    #             if not next_state.is_in_visited(visited):
    #                 # calculate the tentative g value of the next state
    #                 tentative_g = current_state.get_g() + 1
    #                 temp_f_score = tentative_g + next_state.get_h()
    #                 print(next_state.get_g())
    #                 print(next_state.get_f())
    #                 # if the tentative g value is lower than the current g value of the next state
    #                 if temp_f_score < f_map[next_state]:
    #                     print("tentative_g < next_state.get_g()")
    #                     # update the parent and the path of the next state
    #                     parent_map[next_state] = current_state
    #                     next_state.path = current_state.path + [action]
    #                     # calculate the f value of the next state
    #                     next_f = next_state.get_f()
    #                     # insert the next state into the open list as a tuple of (f, h, state)
    #                     heapq.heappush(open_list, (next_f, next_state.get_h(), next_state))
    #                     # update the f value of the next state in the f map
    #                     f_map[next_state] = next_f
    #
    #         # if the open list is empty and the goal state is not found, return None and -1
    #     return None, -1

    # def a_star(self):
    #     # create intial state
    #     initial_state = self.board
    #
    #     # create open list
    #     openList = []
    #     heapq.heapify(openList)
    #
    #     heapq.heappush(openList, initial_state)
    #
    #     gScore = defaultdict(lambda: math.inf)  # create a defaultdict that returns infinity by default
    #     gScore[initial_state] = 0  # set the gScore of the initial state to 0





    # def a_star(self):
    #     # creating the initial state
    #     initial_state = self.board
    #
    #     # creating the open list
    #     openList = []
    #
    #     # creating the closed list
    #     closedList = set()
    #
    #     # adding the start node to the open list
    #     openList.append((initial_state.get_f(), initial_state.get_h(), initial_state))
    #
    #     # creating the predecessors dictionary
    #     predecessors = {}
    #
    #     # while the open list is not empty
    #     while openList:
    #         current_state = self.lowest_f(openList)
    #
    #         # print(current_state)
    #         if current_state.is_solved():
    #             self.solved = True
    #             self.moves = []
    #             self.moves.append(current_state)
    #             print("Solved")
    #             # current_state=current_state[2]
    #             # print(current_state in predecessors)
    #             while predecessors[current_state] is not None:
    #                 self.moves.append(predecessors[current_state])
    #                 current_state = predecessors[current_state]
    #             self.moves.reverse()
    #             break
    #         openList.remove(openList[0])
    #         closedList.add(tuple(map(tuple, current_state.board)))
    #
    #         for row in range(self.board.rows):
    #             for col in range(self.board.cols):
    #                 new_state = current_state.copy()
    #                 new_state.toggle_light(row, col)
    #                 if new_state.is_in_visited(closedList) is False:
    #                     openList.append((new_state.get_f(), new_state.get_h(), new_state))
    #                     predecessors[new_state] = current_state
    #                 else:
    #                     print("already visited")


    # def a_star(self):
    #     start= self.board
    #     g_score = defaultdict(lambda: math.inf)
    #     g_score[start] = 0
    #     f_score = defaultdict(lambda: math.inf)
    #     f_score[start] = start.get_h()
    #
    #
    #     openList = PriorityQueue()
    #     openList.put((start.get_h(),start.get_h(), start))
    #
    #     while not openList.empty():
    #         currentState = openList.get()[2]
    #         if currentState.is_solved():
    #             self.solved = True
    #             self.moves = []
    #             self.moves.append(currentState)
    #             print("Solved")
    #             break
    #
    #         for row in range(self.board.rows):
    #             for col in range(self.board.cols):
    #                 next_state = currentState.copy()
    #                 next_state.toggle_light(row, col)
    #                 temp_g_score = g_score[currentState] + 1
    #                 temp_f_score = temp_g_score + next_state.get_h()
    #
    #                 if temp_f_score < f_score[next_state]:
    #                     g_score[next_state] = temp_g_score
    #                     f_score[next_state] = temp_f_score
    #                     openList.put((temp_f_score, temp_g_score, next_state))



        # while openList:
        #     # get the node with the lowest f value
        #     current_node= self.lowest_f(openList)
        #     print(current_node)
        #
        #     # if the current node is the solution
        #     if current_node.is_solved():
        #         self.solved = True
        #         print("Solved!")
        #         return current_node.path
        #         # break
        #
        #
        # openList.remove(current_node)
        # closedList.add(tuple(map(tuple, current_node.board)))
        #
        # # for each possible move
        # for row in range(self.board.rows):
        #     for col in range(self.board.cols):
        #         # create a copy of the current state
        #         new_state = current_node.copy()
        #         # make the move on the copy
        #         new_state.toggle_light(row, col)



# create main

if __name__ == "__main__":
    # create a game board with 2 rows and 4 columns
    board = GameBoard.GameBoard(2, 4)
    # create a solver using the A* algorithm
    solver = LightsOutSolver_AStar(board)
    # print the initial state of the board
    print("Initial state:")
    print(board)
    # solve the board and get the solution path and the number of moves
    path, moves = solver.a_star()
    # if the solution is found
    if path is not None:
        # print the solution path and the number of moves
        print("Solution path:")
        for state in path:
            print(state)
        print(f"Number of moves: {moves}")
    # if the solution is not found
    else:
        # print a message that the board is unsolvable
        print("The board is unsolvable.")
