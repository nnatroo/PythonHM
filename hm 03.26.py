"""Exercise N1"""

# class Cat:
#
#     def eat(self):
#         print(f'Cat eats a milk')
#
#     def talk(self):
#         print(f'Cat says miaww')
#
#     def walk(self):
#         print(f'Cat can run 20km/h')
#
#
# class Dog:
#
#     def eat(self):
#         print(f'Dog eats a bone')
#
#     def talk(self):
#         print(f'Dog says awww')
#
#     def walk(self):
#         print(f'Dog can run 40km/h')
#
#
# c1 = Cat()
# d1 = Dog()
#
# for _ in (c1, d1):
#     _.eat()
#     _.talk()
#     _.walk()


"""Exercise N2"""

# class Currency(object):
#     dictCurrencies = {"GEL": {"USD": 0.31, "EUR": 0.28},
#                       "USD": {"GEL": 3.22, "EUR": 0.91},
#                       "EUR": {"GEL": 3.55, "USD": 1.1}}
#
#     def __init__(self, value=0.00, unit="GEL"):
#         self.value = value
#         self.unit = unit
#
#     def __str__(self):
#         return f'{round(float(self.value), 2)} {self.unit}'
#
#     def changeTo(self, otherUnit):
#         multiplierValue = self.dictCurrencies[self.unit][otherUnit]
#         return f"{round(self.value * multiplierValue, 2)} {otherUnit}"
#
#     def __add__(self, other):
#         if isinstance(other, Currency):
#             if self.unit == other.unit:
#                 return f'{self.value + other.value} {self.unit}'
#             elif self.unit != other.unit:
#                 multiplierValue = other.dictCurrencies[other.unit][self.unit]
#                 convertedValue = other.value * multiplierValue
#                 return f'{round(self.value + convertedValue, 2)} {self.unit}'
#             else:
#                 print("Unexpected Error")
#
#         else:
#             return f'{self.value + other} {self.unit}'
#
#     def __radd__(self, other):
#         return f'{self.value + other} {self.unit}'
#
#     def __mul__(self, scaleNumb):
#         if isinstance(scaleNumb, int) or isinstance(scaleNumb, float):
#             return f'{self.value * scaleNumb} {self.unit}'
#
#         else:
#             raise TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე")
#
#     def __rmul__(self, scaleNumb):
#         if isinstance(scaleNumb, int) or isinstance(scaleNumb, float):
#             return f'{self.value * scaleNumb} {self.unit}'
#         else:
#             raise TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე")
#
#
# c1 = Currency(1200, "USD")
# # print(c1)
# # print(c1.changeTo("GEL"))
# # print(c1.changeTo("EUR"))
#
# # print("\n")
#
# c2 = Currency(2500, "GEL")
# # print(c2)
# # print(c2.changeTo("USD"))
# # print(c2.changeTo("EUR"))
#
# c5 = c1 * 4
#
#
# c3 = Currency(2000, "GEL")
# c4 = Currency(3500, "GEL")
#
# print(100 + c1)
# # c5 = c1 + c2
# # print(c5)


"""Exercise N3"""


# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan
#
#     def __str__(self):
#         return f'Name : {self.name}\n' \
#                f'Deposit : {self.deposit}\n' \
#                f'Loan : {self.loan}\n'
#
#
# class House:
#     def __init__(self, ID, price, owner, status="გასაყიდი"):
#         self.ID = ID
#         self.price = price
#         self.owner = owner
#         self.status = status
#
#     def __str__(self):
#         return f'ID : {self.ID}\n' \
#                f'Price : {self.price}\n' \
#                f'Owner : {self.owner.name}\n' \
#                f'Status : {self.status}\n'
#
#     def sell(self, buyer, loan=None):
#         if loan is None:
#             self.owner.deposit += self.price
#             self.owner = buyer
#             self.status = "გაყიდული"
#             buyer.deposit -= self.price
#             print(f'!- ბინა გაყიდულია -! \n{self.__str__()}')
#
#         else:
#             self.owner.deposit += self.price
#             self.owner = buyer
#             self.status = "გაყიდულია სესხით"
#             buyer.loan += loan
#             if loan < self.price:
#                 fromDeposit = self.price - loan
#                 buyer.deposit -= fromDeposit
#             print(f'!- ბინა გაყიდულია -! \n{self.__str__()}')


# seller_p1 = Person("John Kennedy", 150000, 30000)
# # buyer_p2 = Person("Donuld Trump", 300000, 60000)
# # h1 = House("01.11.05.031.001", 60000, seller_p1)
# #
# # print(seller_p1)
# # print(buyer_p2)
# # print(h1)
# #
# # print("-------------- After sell operation -------------\n")
# # h1.sell(buyer_p2)
# #
# # print(seller_p1)
# # print(buyer_p2)

# seller_p1 = Person("John Kennedy", 150000, 30000)
# buyer_p2 = Person("Donuld Trump", 300000, 60000)
# h1 = House("01.11.05.031.001", 60000, seller_p1)
#
# print(seller_p1)
# print(buyer_p2)
# print(h1)
#
# print("-------------- After sell operation -------------\n")
# h1.sell(buyer_p2, 40000)
#
# print(seller_p1)
# print(buyer_p2)
#
