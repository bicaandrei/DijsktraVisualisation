class RepoLines:

    def __init__(self):

        self.__lines = []

    def add_line(self, line):

        self.__lines.append(line)

    def delete_line(self, line):

        if line in self.__lines:
            self.__lines.remove(line)

    def get_all_lines(self):

        line_copy = []
        for line in self.__lines:
            line_copy.append(line)
        return line_copy