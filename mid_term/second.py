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
            for col in range(1, self.cols + 1):
                seat_id = f"{row}{chr(64 + col)}"
                self.seats[seat_id] = {'status': 'available', 'customer': None}

class Star_Cinema:
    hall_list = []

    def __init__(self, hall):
        Star_Cinema.hall_list.append(hall)

hall1 = Hall(rows=10, cols=15, hall_no=1)
hall2 = Hall(rows=8, cols=12, hall_no=2)

cinema1 = Star_Cinema(hall1)
cinema2 = Star_Cinema(hall2)

print(Star_Cinema.hall_list)