class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):

        self.hall_list.append(hall)


hall1 = Hall("Hall 1", 100)
hall2 = Hall("Hall 2", 200)

star_cinema = Star_Cinema()
star_cinema.entry_hall(hall1)
star_cinema.entry_hall(hall2)

print(f"Halls in Star Cinema: {star_cinema.hall_list}")