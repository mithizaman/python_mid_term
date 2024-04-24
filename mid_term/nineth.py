class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {} 
        self._show_list = [] 
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

    def _initialize_seats(self):
        for row in range(1, self._rows + 1):
            self._seats[row] = ['free' for _ in range(1, self._cols + 1)]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['free' for _ in range(1, self._cols + 1)] for _ in range(1, self._rows + 1)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            print("Error: Show ID not found.")
            return

        for seat in seat_list:
            row, col = seat
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print(f"Error: Invalid seat: {seat}")
                continue

            if self._seats[show_id][row - 1][col - 1] == 'booked':
                print(f"Error: Seat {seat} is already booked.")
            else:
                self._seats[show_id][row - 1][col - 1] = 'booked'
                print(f"Seat {seat} booked successfully.")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print("Error: Show ID not found.")
            return

        print(f"Available seats for show {show_id}:")
        for row in range(1, self._rows + 1):
            for col in range(1, self._cols + 1):
                if self._seats[show_id][row - 1][col - 1] == 'free':
                    print(f"Row: {row}, Column: {col}")

    def view_show_list(self):
        print("Shows Running:")
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")


class Counter:
    def __init__(self, hall):
        self._hall = hall

    def view_all_shows(self):
        self._hall.view_show_list()

    def view_available_seats(self, show_id):
        self._hall.view_available_seats(show_id)

    def book_tickets(self, show_id, seat_list):
        self._hall.book_seats(show_id, seat_list)


hall1 = Hall(rows=10, cols=15, hall_no=1)
hall1.entry_show("S1", "The Matrix", "12:00 PM")
hall1.entry_show("S2", "Inception", "3:00 PM")

counter = Counter(hall1)

print("Viewing all shows:")
counter.view_all_shows()

print("\nViewing available seats for show S1:")
counter.view_available_seats("S1")

print("\nBooking tickets for show S1:")
counter.book_tickets("S1", [(1, 2), (3, 4), (15, 16)]) 
counter.book_tickets("S1", [(1, 2), (3, 4), (5, 6)])