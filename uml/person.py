class Person:

    def __init__(self, name, phone_number, email_address, card_number):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.__card_number = card_number

    def book_hotel(self):
        pass
