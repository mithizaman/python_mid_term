def __init__(self, rows, cols, hall_no):
        self.seats = {} 
        self.show_list = [] 
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.initialize_seats()

    def initialize_seats(self):
        for row in range(1, self.rows + 1):
            self.seats[row] = ['free' for _ in range(1, self.cols + 1)]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [['free' for _ in range(1, self.cols + 1)] for _ in range(1, self.rows + 1)]
