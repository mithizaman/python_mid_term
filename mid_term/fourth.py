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

    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print("Show ID not found.")
            return

        for seat in seat_list:
            row, col = seat
            if row < 1 or row > self.rows or col < 1 or col > self.cols:
                print(f"Invalid seat: {seat}")
                continue

            if self.seats[show_id][row - 1][col - 1] == 'booked':
                print(f"Seat {seat} is already booked.")
            else:
                self.seats[show_id][row - 1][col - 1] = 'booked'
                print(f"Seat {seat} booked successfully.")

class Star_Cinema:
    hall_list = []

    def __init__(self, hall):
        Star_Cinema.hall_list.append(hall)


hall1 = Hall(rows=10, cols=15, hall_no=1)
hall1.entry_show("S1", "The Matrix", "12:00 PM")

hall1.book_seats("S1", [(1, 2), (3, 4), (5, 6)])
hall1.book_seats("S1", [(1, 2), (3, 4), (5, 6)])
hall1.book_seats("S2", [(1, 2), (3, 4), (5, 6)])

print(hall1.seats["S1"])