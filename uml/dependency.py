class Computer:
    pass


class Person:

    def send_email(self, computer: Computer):
        pass


if __name__ == '__main__':
    person = Person()
    computer = Computer()
    person.send_email(computer)
