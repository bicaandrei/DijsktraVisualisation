import pygame

from errors.RepoError import RepoError

class RepoNodes:

    def __init__(self):

        self.__nodes = {}
        self.__rects = {}

    def add_node(self, node, rect):

        id = node.get_id()
        ok = True
        for id_rect in self.__rects:
            if pygame.Rect.colliderect(rect, self.__rects[id_rect]) == True:
                ok = False
        if ok:
           self.__rects[id] = rect
           self.__nodes[id] = node
        return ok

    def delete_node(self, id):

        if id in self.__nodes:
            del self.__nodes[id]
            del self.__rects[id]

    def get_all_nodes(self):

        nodes_copy = []
        for id_node in self.__nodes:
            nodes_copy.append(self.__nodes[id_node])
        return nodes_copy

