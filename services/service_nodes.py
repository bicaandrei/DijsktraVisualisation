import math

import pygame
from domain.Nodes import Node
import sys
from services.service_lines import ServiceLines

class ServiceNodes:

    def __init__(self, repo_nodes):

        self.repo_nodes = repo_nodes

    def add_node(self, id, x, y):

        node = Node(id, x, y)
        rect = pygame.Rect(x-15, y-15, 30, 30)
        return self.repo_nodes.add_node(node, rect)

    def find_node(self, id_node):

        nodes = self.repo_nodes.get_all_nodes()
        for node in nodes:
            if node.id == id_node:
                return node

    def verify_node(self, x, y):

        nodes = self.repo_nodes.get_all_nodes()
        for node in nodes:
            if (node.x - 15 <= x <= node.x + 15) and (node.y - 15 <= y <= node.y + 15):
                return node.id, node.x, node.y
        return -1, -1, -1

    def delete_node(self, id):

        self.repo_nodes.delete_node(id)

    def get_all_nodes(self):

        return self.repo_nodes.get_all_nodes()

    def dijkstra_algorithm(self, nodes, start_node):
        unvisited_nodes = nodes

        shortest_path = {}

        previous_nodes = {}

        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node.id] = max_value

        shortest_path[start_node.id] = 0

        while unvisited_nodes:

            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node.id] < shortest_path[current_min_node.id]:
                    current_min_node = node

            neighbors = current_min_node.get_neighbors()
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node.id] + ServiceLines.get_length_line(self, current_min_node.x, current_min_node.y, neighbor.x, neighbor.y)
                if tentative_value < shortest_path[neighbor.id]:
                    shortest_path[neighbor.id] = tentative_value

                    previous_nodes[neighbor.id] = current_min_node

            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path

    def print_result(self, previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node

        while node != start_node:
            path.append(node.id)
            node = previous_nodes[node.id]

        path.append(start_node.id)
        path.reverse()
        return path