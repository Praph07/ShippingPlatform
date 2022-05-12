from extra import test_email


class User:
    def __init__(self, firstname, lastname, email, address):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if test_email(email) is False:
            raise ValueError('Email format is invalid')
        self._email = email

    @classmethod
    def get_user_detail(cls):

        while True:
            firstname = str(input("First Name:"))
            if firstname == '':
                print('First Name cannot be left blank. \n')
                continue
            else:
                break
        while True:
            lastname = str(input("Last Name:"))
            if lastname == '':
                print('Last Name cannot be left blank. \n')
                continue
            else:
                break
        while True:
            email = input("Email:")
            if test_email(email) is True:
                break
            else:
                print("Please enter a valid email.")
                continue
        while True:
            address = str(input("Address:"))
            if address == '':
                print('Address cannot be left blank. \n')
                continue
            else:
                break
        return cls(firstname, lastname, email, address)


class Sender(User):

    def __init__(self, firstname, lastname, email, address):
        super().__init__(firstname, lastname, email, address)


class Receiver(User):

    def __init__(self, firstname, lastname, email, address):
        super().__init__(firstname, lastname, email, address)


__all__ = ["User", "Sender", "Receiver"]
