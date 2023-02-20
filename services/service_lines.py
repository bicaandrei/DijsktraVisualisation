from domain.Lines import Lines
import math

class ServiceLines:

    def __init__(self, repo_lines):

        self.__repo_lines = repo_lines

    def add_line(self, start_x, start_y, end_x, end_y):

        line = Lines(start_x, start_y, end_x, end_y, 1)
        self.__repo_lines.add_line(line)

    def get_length_line(self, start_x, start_y, end_x, end_y):

        dist = (end_x - start_x) * (end_x - start_x)
        dist += (end_y - start_y) * (end_y - start_y)
        dist = math.sqrt(dist)
        return dist

    def delete_line(self, start_x, start_y, end_x, end_y):

        line = Lines(start_x, start_y, end_x, end_y, 1)
        self.__repo_lines.delete_line(line)

    def get_all_lines(self):

        return self.__repo_lines.get_all_lines()