class Node:
    def __init__(self, state):
        self.state = state
        self.zero_pos = None
        self.length = len(self.state) #taking this will help us to change the code for other puzzle as well
        self.find_zero()

        self.f_cost = 0
        self.g_cost = 0
        self.h_cost = 0

    def __repr__(self):
        return f"Node <{self.state}>"

    def __lt__(self, otherNode):
        return self.f_cost < + otherNode.f_cost

    #now we will find the index in grid with zero in it
    def find_zero(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.state[i][j] == 0:
                    self.zero_pos = (i, j)

    def get_state(self):
        return self.state

    def get_zero_pos(self):
        return self.zero_pos

    def print_state(self):
        for row in self.state:
            print(" ".join(str(x) for x in row))
    
    def get_row_col(self, state, num):
        row = 0
        while num >= self.width:
            num -= self.width
            row += 1
        col = num
        return row, col

    def set_f_cost(self, f_cost):
        self.f_cost = f_cost
    
    def get_f_cost(self):
        return self.f_cost

    def set_g_cost(self, g_cost):
        self.g_cost = g_cost

    def get_g_cost(self):
        return self.g_cost

    def set_h_cost(self, h_cost):
        self.h_cost = h_cost

    def get_h_cost(self):
        return self.h_cost