"""Exercise N1"""

# class People:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.uni@btu.edu.ge'
#
#     def __str__(self):
#         return f'{self.firstname}, {self.lastname}'
#
#
# class Lecturer(People):
#     def __init__(self, firstname, lastname, salary):
#         super().__init__(firstname, lastname)
#         self.salary = salary
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}@btu.edu.ge'
#
#     def __str__(self):
#         return f'{self.firstname}, {self.lastname}, {self.salary}'
#
#
# class Student(People):
#     def __init__(self, firstname, lastname, courses):
#         super().__init__(firstname, lastname)
#         self.courses = courses
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.1@btu.edu.ge'
#
#     def __str__(self):
#         return f'{self.firstname}, {self.lastname}, {self.courses}'
#
#
# s1 = Student("Nugo", "Natroshvili", ["Calkulus", "Python", "Oracle", "PC Architect", "Management", "Startups"])
# print(S1)
# print(s1.get_email())
#
# print("\n")
#
# l1 = Lecturer("Nicolas", "Walker", 2200)
# print(l1)
# print(l1.get_email())
#
# p1 = People("Elon", "Musk")
# print(p1)
# print(p1.get_email())


"""Exercise N2 ( Library )"""

# class LibraryItem:
#     def __init__(self, title, subject, status):
#         self.title = title
#         self.subject = subject
#         self.status = status
#
#     def booking(self):
#         if self.status == "available":
#             self.status = "occupied"
#             print(f'Item successfully booked ! ')
#
#         else:
#             print(f'Item isn`t available for booking ! ')
#
#
# class Book(LibraryItem):
#     def __init__(self, ISBN, authors, title, subject, status):
#         super().__init__(title, subject, status)
#         self.ISBN = ISBN
#         self.authors = authors
#
#     def __str__(self):
#         return f'{self.ISBN},\n{self.authors},\n{self.title},\n{self.subject},\n{self.status}'
#
#
# class Magazine(LibraryItem):
#     def __init__(self, journalName, volume, status):
#         self.journalName = journalName
#         self.volume = volume
#         super().__init__(status)
#
#
# class CD(LibraryItem):
#     def __init__(self, title, status):
#         super().__init__(title, status)
#
#     def booking(self):
#         print(f'CD`s Booking isn`t available now ! Try later !')
#
#
# b1 = Book(123456789, "J. K. Rowling", "Harry Potter", "Fantasy", "available")
# print(b1)
# b1.booking()
# print(b1.status)
# b1.booking()
# b1.booking()


'''Exercise N3 ( Contact Manager )'''

# class Contacts:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#
# class MailSender:
#     def __init__(self, email):
#         self.email = email
#
#     def send_mail(self):
#         print(f'თქვენი მეილი გაიგზავნა ამ მისამართზე: {self.email}')
#
#
# class Friend(Contacts, MailSender):
#     def __init__(self, name, phone, email):
#         super().__init__(name, phone)
#         self.email = email
#
#     def __str__(self):
#         return f'Name : {self.name}\n' \
#                f'Phone : {self.phone}\n' \
#                f'Email : {self.email}'
#
#
# class Family(Contacts, MailSender):
#     def __init__(self, name, email, phone, birthdate="01/01/0001"):
#         super().__init__(name, phone)
#         self.email = email
#         self.birthdate = birthdate
#
#
# f1 = Friend("Nicolas", 599000000, "natroshvili@gmail.com")
# print(f1.email, f1.name, f1.phone)
# f1.send_mail()
# print(f1)


'''Exercise N4 ( University with Diamond Problem ) '''

# class People:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.uni@btu.edu.ge'
#
#     def __str__(self):
#         return f'{self.firstname}, {self.lastname}'
#
#
# class Lecturer(People):
#     def __init__(self, firstname, lastname, salary):
#         super().__init__(firstname, lastname)
#         self.salary = salary
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}@btu.edu.ge'
#
#     def __str__(self):
#         return f'{self.firstname}, {self.lastname}, {self.salary}'
#
#
# class Student(People):
#     def __init__(self, firstname, lastname, courses):
#         super().__init__(firstname, lastname)
#         self.courses = courses
#
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.1@btu.edu.ge'
#
#     def __str__(self):
#         return f'{self.firstname}, {self.lastname}, {self.courses}'
#
#
# class Doctoral_student(Lecturer, Student):
#     def __init__(self, firstname, lastname, salary, courses):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#         self.courses = courses
#
#     def __str__(self):
#         return f'First Name : {self.firstname}\n' \
#                f'Last Name : {self.lastname} \n' \
#                f'Salary : {self.salary}\n' \
#                f'Courses : {self.courses} \n'
#
#     '''Override'''
#     def get_email(self):
#         return f'{self.firstname}.{self.lastname}.PhD@btu.edu.ge'
#
#
# d1 = Doctoral_student("Nugo", "Natroshvili", "4000", "Math")
# print(d1)
# print(d1.get_email())
