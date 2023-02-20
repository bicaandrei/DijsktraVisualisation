class Node:

    def __init__(self, id, x, y):

        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []

    def get_id(self):

        return self.id

    def get_pos(self):

        return self.x, self.y

    def set_neighbors(self, neighbor):

        self.neighbors.append(neighbor)

    def delete_neighbor(self, neighbor):

        self.neighbors.remove(neighbor)

    def get_neighbors(self):

        return self.neighbors