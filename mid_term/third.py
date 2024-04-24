class Hall:
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


class Star_Cinema:
    hall_list = []

    def __init__(self, hall):
        Star_Cinema.hall_list.append(hall)


hall1 = Hall(rows=10, cols=15, hall_no=1)
hall1.entry_show("S1", "The Matrix", "12:00 PM")
hall1.entry_show("S2", "Inception", "3:00 PM")

print(hall1.show_list)
print(hall1.seats)
