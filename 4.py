class Ticket:
    def __init__(self, movie_name, price, quantity):
        self.movie_name = movie_name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def show_info(self):
        print(f"Film: {self.movie_name}")
        print(f"Chipta narxi: {self.price}")
        print(f"Soni: {self.quantity}")
        print(f"Umumiy narx: {self.total_cost()}")


ticket = Ticket("Avatar", 40000, 3)
print(ticket.total_cost())  # 120000