from datetime import datetime


class Card:
    def __init__(self, card_num, expiry, holder_name, balance):
        self.card_num = card_num
        self.expiry = expiry
        self.holder_name = holder_name
        self.balance = balance

    @property
    def card_num(self):
        return self.card_num

    @card_num.setter
    def card_num(self, value):
        if type(value) is not int:
            raise ValueError('Please enter a numeric value.')
        elif len(str(value)) != 16:
            raise ValueError("Please enter a 16 digit card number.")
        else:
            self.value = value

    @classmethod
    def card_input(cls):
        while True:
            print('Please enter your card details: \n'
                  f'{"*" * 40}')
            try:
                card_num = int(input("16 digit card number:"))
                if len(str(card_num)) != 16:
                    print("Those are not 16 digit! Please enter a 16 digit card number!")
                    continue
                else:
                    while True:
                        expiry = None
                        try:
                            expiry = datetime.strptime(input("Card expiry date (mm/yy):"), "%m/%y")
                            if expiry < datetime.today():
                                print("Your card has already expired! Please enter a new card.")
                                break
                            else:
                                break
                        except ValueError:
                            print("Please enter a valid date with correct format (mm/yy)!")
                            continue
                    if expiry < datetime.today():
                        continue
                    else:
                        holder_name = input("Card Holder Name (FirstName LastName):")
                        while True:
                            try:
                                balance = float(input("Card balance($):"))
                                break
                            except ValueError:
                                print('Card balance has to be numeric!')

                        print(f'Your card details have been saved.\n')

                        return cls(card_num, expiry, holder_name, balance)
            except ValueError:
                print("Invalid Card Number!")
                continue

    def deduce_balance(self, value):
        new_balance = self.balance - value
        self.balance = new_balance
        return self.balance
