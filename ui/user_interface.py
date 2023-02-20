import time

import pygame
import sys
from domain.Nodes import Node

pygame.font.init()

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
    "green": (50, 205, 0),
    "blue": (30, 144, 255),
    "color_light": (170, 170, 170),
    "color_dark": (100, 100, 100),
    "red": (238, 75, 43)
}

class UI:

    def __init__(self, service_nodes, service_lines, width, height):

        self.service_nodes = service_nodes
        self.service_lines = service_lines
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        self.smallfont = pygame.font.SysFont('Corbel', 20)
        self.node_id = [False for i in range(0, 26)]
        self.continue_algorithm = -1
        self.start_node = None

    def menu(self):

        loop = True
        smallfont = pygame.font.SysFont('Corbel', 35)
        textCompute = smallfont.render('Start', True, colors["red"])
        while loop:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.width/2-125 <= mouse[0] <= self.width/2+160 and self.height/2-105 <= mouse[1] <= self.height/2-55:
                        loop = False
                        break

            if self.width / 2 - 135 <= mouse[0] <= self.width / 2 + 160 and self.height / 2 - 105 <= mouse[1] <= self.height / 2-55:
                pygame.draw.rect(self.window, colors["color_light"], [self.width/2-135, self.height/2-105, 295, 50])
            else:
                pygame.draw.rect(self.window, colors["color_dark"], [self.width/2-135, self.height/2-105, 295, 50])

            self.window.blit(textCompute, (self.width/2-20, self.height/2-100))
            pygame.display.update()


    def run(self):

        pygame.display.set_caption("Dijkstra Visualisation")
        self.window.fill(colors["white"])
        pygame.display.update()
        cnt = 0
        cnt2 = 0
        color = "white"
        dijsktra = False
        self.menu()
        self.window.fill(colors["white"])
        pygame.display.flip()
        while True:

            if dijsktra == True:

                time.sleep(2)
                nodes = self.service_nodes.get_all_nodes()
                for node in nodes:
                    pygame.draw.circle(self.window, colors["white"], (node.x, node.y), 15)
                    pygame.draw.circle(self.window, colors["black"], (node.x, node.y), 15, 1)
                    textid = self.smallfont.render(chr(node.id + 65), True, colors["black"])
                    self.window.blit(textid, (node.x - 6, node.y - 7))
                dijsktra = False

            pygame.display.flip()
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == True:

                        mouse_x = mouse[0]
                        mouse_y = mouse[1]
                        exists, x, y = self.service_nodes.verify_node(mouse_x, mouse_y)
                        if exists == -1:
                           for i in range(0, 26):
                                if self.node_id[i] == False:
                                   ok = self.service_nodes.add_node(i, mouse_x, mouse_y)
                                   if ok:
                                      self.node_id[i] = True
                                      textid = self.smallfont.render(chr(i+65), True, colors["black"])
                                      self.window.blit(textid, (mouse_x-6, mouse_y-7))
                                      pygame.draw.circle(self.window, colors["black"], (mouse_x, mouse_y), 15, 1)
                        else:

                           if cnt == 0:

                              id_neigbor1, line_start_x, line_start_y = self.service_nodes.verify_node(mouse[0], mouse[1])
                              nodes = self.service_nodes.get_all_nodes()
                              for node in nodes:
                                  pygame.draw.circle(self.window, colors["green"], (node.x, node.y), 15)
                                  textid = self.smallfont.render(chr(node.id + 65), True, colors["black"])
                                  self.window.blit(textid, (node.x - 6, node.y - 7))
                              color = "green"
                              cnt = 1

                           elif cnt == 1:

                              id_neigbor2, line_end_x, line_end_y = self.service_nodes.verify_node(mouse[0], mouse[1])
                              pygame.draw.line(self.window, colors["black"], (line_start_x, line_start_y), (line_end_x, line_end_y))
                              self.service_lines.add_line(line_start_x, line_start_y, line_end_x, line_end_y)
                              nodes = self.service_nodes.get_all_nodes()

                              node1 = self.service_nodes.find_node(id_neigbor1)
                              node2 = self.service_nodes.find_node(id_neigbor2)
                              node1.set_neighbors(node2)
                              node2.set_neighbors(node1)

                              for node in nodes:
                                  pygame.draw.circle(self.window, colors["white"], (node.x, node.y), 15)
                                  pygame.draw.circle(self.window, colors["black"], (node.x, node.y), 15, 1)
                                  textid = self.smallfont.render(chr(node.id + 65), True, colors["black"])
                                  self.window.blit(textid, (node.x - 6, node.y - 7))
                              color = "white"
                              cnt = 0


                    elif pygame.mouse.get_pressed()[2] == True:

                         id, x, y = self.service_nodes.verify_node(mouse[0], mouse[1])

                         if id != -1:

                             nodes = self.service_nodes.get_all_nodes()
                             for node in nodes:
                                 if node.id == id:
                                     node_x, node_y = node.get_pos()
                                     node_neighbors = node.get_neighbors()
                                     for neighbor in node_neighbors:
                                         pygame.draw.line(self.window, colors["white"], (node_x, node_y),(neighbor.x, neighbor.y))
                                         self.service_lines.delete_line(node_x, node_y, neighbor.x, neighbor.y)
                                         self.service_lines.delete_line(neighbor.x, neighbor.y, node_x, node_y)
                                     for neighbor in node_neighbors:
                                         neighbor.delete_neighbor(node)

                                     break

                             lines = self.service_lines.get_all_lines()
                             for line in lines:
                                 pygame.draw.line(self.window, colors["black"], (line.start_x, line.start_y),
                                                  (line.end_x, line.end_y))

                             for node in nodes:
                                 if color == "green":
                                    pygame.draw.circle(self.window, colors["green"], (node.x, node.y), 15)
                                    textid = self.smallfont.render(chr(node.id + 65), True, colors["black"])
                                    self.window.blit(textid, (node.x - 6, node.y - 7))
                                 else:
                                    pygame.draw.circle(self.window, colors["white"], (node.x, node.y), 15)
                                    pygame.draw.circle(self.window, colors["black"], (node.x, node.y), 15, 1)
                                    textid = self.smallfont.render(chr(node.id + 65), True, colors["black"])
                                    self.window.blit(textid, (node.x - 6, node.y - 7))

                             self.service_nodes.delete_node(id)
                             self.node_id[id] = False
                             pygame.draw.circle(self.window, colors["white"], (x, y), 15)

                    elif pygame.mouse.get_pressed()[1] == True:

                         if cnt2 == 0:

                            nodes = self.service_nodes.get_all_nodes()

                            id_start_node, start_node_x, start_node_y = self.service_nodes.verify_node(mouse[0], mouse[1])
                            self.start_node = self.service_nodes.find_node(id_start_node)
                            cnt2 = 1
                            if id_start_node != -1:
                                self.continue_algorithm = 1
                            else:
                                cnt2 = 0

                         elif cnt2 == 1 and self.continue_algorithm != -1:

                            nodes = self.service_nodes.get_all_nodes()
                            previous_nodes, shortest_path = self.service_nodes.dijkstra_algorithm(nodes, self.start_node)
                            id_target_node, target_node_x, target_node_y = self.service_nodes.verify_node(mouse[0], mouse[1])

                            if id_target_node != -1:
                               target_node = self.service_nodes.find_node(id_target_node)
                               path = self.service_nodes.print_result(previous_nodes, shortest_path, self.start_node, target_node)
                               i = 0
                               for id in path:
                                   node = self.service_nodes.find_node(id)
                                   if i > 1:
                                      time.sleep(1)
                                   pygame.display.flip()
                                   pygame.draw.circle(self.window, colors["blue"], (node.x, node.y), 15)
                                   textid = self.smallfont.render(chr(node.id + 65), True, colors["black"])
                                   self.window.blit(textid, (node.x - 6, node.y - 7))
                                   i += 1
                               dijsktra = True

                            cnt2 = 0
                            self.continue_algorithm = -1

            pygame.display.update()


