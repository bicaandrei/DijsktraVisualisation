class Lines:

    def __init__(self, start_x, start_y, end_x, end_y, color):

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color

    def __eq__(self, other):

        if self.start_x == other.start_x and self.start_y == other.start_y and self.end_x == other.end_x and self.end_y == other.end_y:
            return True


