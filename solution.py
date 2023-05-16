from time import time
from queue import PriorityQueue
from Node import Node
from copy import deepcopy

class Solution(object):
    def __init__(self, initialState):
        self.initialState = initialState #initial state of the puzzle that user selected
        self.length = len(self.initialState)
        #the goal state that we want to reach
        self.goalState = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '0']
        ]
        self.startTime = time() #we will record the start time of the algorithm
        self.visited = set() #we will record all the visited nodes.
        self.frontier = PriorityQueue()
        self.current_frontier = set() #this set will hold the nodes that are currently in the frontier

        #using a flag as false for all the algorithm  and only make it true when we are using any particular algorithm, as we can not use more than one algorithm at any point
        self.uniform = False 
        self.misplaced = False
        self.manhattan = False


    #setting the algorithm selected by the user
    #this will just inverse the flag for the selected algorithm and we can start with our general-search algorithm
    def uniform_cost_search(self):
        self.uniform = True
        self.general_search()

    def misplaced_search(self):
        self.misplaced = True
        self.general_search()
    
    def manhattan_search(self):
        self.manhattan = True
        self.general_search()
    
    def general_search(self):
        #adding the initial state in the queue 
        self.frontier.put(Node(self.initialState))
        max_frontier_size = 1
        num_nodes_expanded = 1
        # self.visited.add(self.initialState)

        while True:
            #the loop will run until we have found the goal state or when the priority queue is empty
            if self.frontier.qsize() == 0:
                print("there's a problem in the inputs")
                break
            current_node = self.frontier.get()
            # print()
            print(f"The best state to expand with a g(n) = {current_node.get_g_cost()} and h(n) = {current_node.get_h_cost()} is ...")
            current_node.print_state()
            if current_node.get_state() == self.goalState:
                executionEnd = time()
                timeTaken = executionEnd - self.startTime

                #printing the results
                print("Goal State Achieved!!!!!")
                print(f"Number of expanded nodes: {num_nodes_expanded}.")
                print(f"The maximum queue size: {max_frontier_size}.")
                print(f"Solution found at depth: {current_node.get_g_cost()}.")
                print(f"Time to finish: {round(timeTaken,2)} second(s).")
                break

            self.current_frontier.discard(current_node)
            # self.visited.add(current_node)
            neighbors = self.expand(current_node)

            for neighbor in neighbors:
                if not neighbor in self.current_frontier:
                # if neighbor not in self.visited and neighbor not in self.current_frontier:
                    self.current_frontier.add(neighbor)
                    num_nodes_expanded += 1 #increases the expanded nodes by 1 in each iteration

                    if self.uniform:
                        neighbor.set_f_cost(current_node.get_g_cost())
                        self.frontier.put(neighbor)
                    
                    elif self.misplaced:
                        misplaced_count = sum([neighbor.get_state()[i][j] != self.goalState[i][j] for i in range(self.length) for j in range(self.length)])
                        neighbor.set_h_cost(misplaced_count)
                        neighbor.set_f_cost(current_node.get_g_cost() + current_node.get_h_cost())
                        self.frontier.put(neighbor)

                    elif self.manhattan:
                        manhattan_distance = 0
                        n = 3  # assuming 3x3 grid

                        for i in range(n):
                            for j in range(n):
                                num = int(neighbor.get_state()[i][j])
                                if num != 0:
                                    goal_row = (num - 1) // n
                                    goal_col = (num - 1) % n
                                    manhattan_distance += abs(i - goal_row) + abs(j - goal_col)

                        neighbor.set_h_cost(manhattan_distance)
                        neighbor.set_f_cost(current_node.get_g_cost() + current_node.get_h_cost())
                        self.frontier.put(neighbor)
            
            max_frontier_size = max(max_frontier_size, self.frontier.qsize())
    
    def inBound(self, i,j):
        return 0<=i<3 and 0<=j<3 #the value = 3 can be changed for different sized puzzle
    
    def expand(self, current_node):
        # if not current_node:
        #     return []
        neighbors = []
        i, j = current_node.get_zero_pos()
        grid = current_node.get_state()

        directions = [(-1,0), (1, 0), (0, -1), (0, 1)] #using simple queue iteration for all the neighbors of empty block

        for di, dj in directions:
            ni, nj = i+di, j+dj

            if self.inBound(ni, nj):
                temp = deepcopy(grid) #creating a code of the grid and swapping the empty(0) element with the potential neighbor
                temp[i][j], temp[ni][nj] = temp[ni][nj], temp[i][j]
                newNode = Node(temp)

                #checking and only adding in the neighbors list if it's not already visited
                if newNode not in self.visited:
                    self.visited.add(newNode)
                    newNode.set_g_cost(current_node.get_g_cost() + 1)
                    neighbors.append(newNode)
        
        return neighbors