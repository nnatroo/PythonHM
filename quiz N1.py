class Ticket:

    def __init__(self, film_name, ticket_price, ticket_amount, language='Geo'):
        self.film_name = film_name
        self.ticket_price = ticket_price
        self.ticket_amount = ticket_amount
        self.language = language

    def __str__(self):
        return f'Film name: {self.film_name}\n' \
               f'Ticket price : {self.ticket_price}\n' \
               f'Ticket amount : {self.ticket_amount}\n' \
               f'Language : {self.language}\n'

    def compare_tickets(self, other):

        #   Compare amounts with each other
        if isinstance(other, Ticket) and self.ticket_amount > other.ticket_amount:
            print(f'At this moment, \"{self.film_name}\" have more tickets than \"{other.film_name}\".\n')

        elif isinstance(other, Ticket) and self.ticket_amount < other.ticket_amount:
            print(f'At this moment, \"{other.film_name}\" have more tickets than \"{self.film_name}\".\n')

        elif isinstance(other, Ticket) and self.ticket_amount == other.ticket_amount:
            print(f'At this moment, \"{other.film_name}\" have same amount of tickets as \"{self.film_name}\".\n')

        #   Compare amount with Numbers
        elif isinstance(other, int) and self.ticket_amount > other:
            print(f"At this moment, \"{self.film_name}\" have more tickets than {other}.")

        elif isinstance(other, int) and self.ticket_amount < other:
            print(f"At this moment, \"{self.film_name}\" have less tickets than {other}.")

        elif isinstance(other, int) and self.ticket_amount == other:
            print(f"At this moment, \"{self.film_name}\" have same amount of tickets ( {other} ).")

        #   For some unexpected error
        else:
            print("Unexpected Error !")


class User:

    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = balance

    def __str__(self):
        return f'Customer name : {self.customer_name}\n' \
               f'Balance : {self.balance}\n'

    def buy_ticket(self, ticket, buy_tickets_amount):
        tickets_full_value = ticket.ticket_price * buy_tickets_amount   # Total value of tickets

        if tickets_full_value <= self.balance and 0 < buy_tickets_amount <= ticket.ticket_amount:
            self.balance -= tickets_full_value  # Decreasing value of balance
            ticket.ticket_amount -= buy_tickets_amount  # Decresing value of tickets amount
            print(f'You bought {buy_tickets_amount} tickets. Film : {ticket.film_name}\n') # Text message for successfully buy operation.

        #   Restrict 0 ticket amount buy order
        elif buy_tickets_amount == 0:
            print("You can`t buy 0 ticket! Ticket amount must be at least 1.\n")

        #   Buy fail reason, when there is insufficient tickets amount
        elif buy_tickets_amount > ticket.ticket_amount:
            print("Insufficient  tickets !\n")

        #   Buy fail reason, when there is insufficient balance
        elif tickets_full_value > self.balance:
            print("Insufficient  balance !\n")

        #   For some unexpected error
        else:
            print("Unexpected Error!")

    #   Method for money deposit to balance
    def deposit(self, deposit_amount):
        if deposit_amount != 0:
            self.balance += deposit_amount
            print(f"You deposited successfully, Your balance is : {self.balance}\n")



"""Checking exercise N1 & 2"""

# t1 = Ticket("Schindler's List", 25, 60, "Eng")
# t2 = Ticket("The Pianist", 20, 60)
#
# print(t1)
# print(t2)


"""Checking exercise N3 & 4"""

# u1 = User("Joe Biden", 2500)
# u2 = User("Donuld Trump", 1500)
#
# print(u1)
# print(u2)


"""Checking exercise N5"""

# #   Cheking successfuly buy operation
# t1 = Ticket("Schindler's List", 25, 60, "Eng")
# u1 = User("Joe Biden", 2500)
#
# print(t1)
# print(u1)
#
# u1.buy_ticket(t1, 25)
#
# print(t1)
# print(u1)


# #   Cheking failed buy operation ( there is not enough tickets )
# t1 = Ticket("Schindler's List", 25, 60, "Eng")
# u1 = User("Joe Biden", 2500)
#
# print(t1)
# print(u1)
#
# u1.buy_ticket(t1, 80)
#
# print(t1)
# print(u1)


# #   Cheking failed buy operation ( there is not enough balance )
# t1 = Ticket("Schindler's List", 25, 60, "Eng")
# u1 = User("Joe Biden", 50)
#
# print(t1)
# print(u1)
#
# u1.buy_ticket(t1, 15)
#
# print(t1)
# print(u1)


"""Checking exercise N6"""

# u1 = User("Joe Biden", 500)
# print(u1)
#
# u1.deposit(1600)
# print(u1)


"""Checking Exercise N7"""

# #   Comparing when ticket amounts aren`t same
# t1 = Ticket("Schindler's List", 25, 60, "Eng")
# t2 = Ticket("The Pianist", 20, 40)
# print(t1)
# print(t2)
#
# t1.compare_tickets(t2)
#
# u1 = User("John Kenneedy", 2500)    #   Test User
# u1.buy_ticket(t1, 30)
#
# print(t1)
# print(t2)
#
# t1.compare_tickets(t2)


# #    Comparing when ticket amount are same
# t1 = Ticket("Schindler's List", 25, 60, "Eng")
# t2 = Ticket("The Pianist", 20, 60)
# print(t1)
# print(t2)
#
# t1.compare_tickets(t2)


# #   Comparing ticket amounts with numbers
# t1 = Ticket("Schindler's List", 25, 60, "Eng")
# t2 = Ticket("The Pianist", 20, 60)
# print(t1)
# print(t2)
#
# t1.compare_tickets(10)
# t2.compare_tickets(80)




# -----------------------------------------------------------
# Practical exercise N1 ( Python )
#
# Natroshvili Nugo
#
# -----------------------------------------------------------