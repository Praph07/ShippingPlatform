from datetime import datetime


def only1or2(user_input, first_param, sec_param):
    while True:
        try:
            user_value = int(input(f'{user_input}:'))
            if user_value not in (1, 2):
                print('INVALID CHOICE!')
            elif user_value == 1:
                print(f'{"_" * 30} \n'
                      f'You have chosen: {first_param} \n'
                      f'{"_" * 30} \n')
                return first_param
            else:
                print(f'{"_" * 30} \n'
                      f'You have chosen: {sec_param} \n'
                      f'{"_" * 30} \n')
                return sec_param

        except ValueError:
            print('INVALID CHOICE!')
            continue


class Shipping:
    def __init__(self, ship_type, method):
        self.ship_type = ship_type
        self.method = method

    def get_method(self):
        return self.method

    @classmethod
    def get_shipping_req(cls):
        ship_type = only1or2("Where are you shipping your package: \n"
                             "Internationally or Locally? \n"
                             "Choose 1 for International and 2 for Local",
                             "International", "Local")
        if ship_type == "International":
            ship_method = only1or2("For International shipping, you have two options for shipping Method: \n"
                                   "Air Shipping and Surface Shipping. \n"
                                   "Choose 1 For Air and 2 For Surface shipping",
                                   "Air", "Surface")

        else:
            ship_method = "Surface"
            print(f"You shipping method will be: {ship_method} \n"
                  "")
        return cls(ship_type, ship_method)

    @classmethod
    def check_rates(cls):
        print(f'The flat rates are as follows: \n'
              f'{"_" * 40} \n'
              f'Rates by shipping type: \n'
              f'\n'
              f'International Shipping: \n'
              f'Priority Worldwide Shipping(2-3 days): ${Shipping.type_price(Shipping("International", ""))[0]} \n'
              f'Express International Shipping(4-7 days): ${Shipping.type_price(Shipping("International", ""))[1]} \n'
              f'Standard Shipping(7-10 days): ${Shipping.type_price(Shipping("International", ""))[2]} \n'
              f'\n'
              f'Local Shipping: \n'
              f'Priority Local Shipping(2-3 days): ${Shipping.type_price(Shipping("Local", ""))[0]} \n'
              f'Express Local Shipping(4-7 days): ${Shipping.type_price(Shipping("Local", ""))[1]} \n'
              f'Standard Local Shipping(7-10 days): ${Shipping.type_price(Shipping("Local", ""))[2]} \n'
              f'{"_" * 40} \n'
              f'Rates by shipping method: \n'
              f'Surface Shipping: ${Shipping.method_price(Shipping("", "Surface"))} \n'
              f'Air Shipping: ${Shipping.method_price(Shipping("", "Air"))} \n'
              f'{"_" * 40} \n'
              f'Rates by package size: \n'
              f'Small Packages (<1m length): ${Package.price_by_size(Package("", "", "Small", "", ""))} \n'
              f'Large Packages (>1m length): ${Package.price_by_size(Package("", "", "Large", "", ""))} \n'
              f'{"_" * 40} \n'
              f'Rates by package weight: \n'
              f'Weight <= 10 kg: ${Package.price_per_weight(Package("", "", "", 10, ""))} per kg \n'
              f'Weight between 10 to 25 kg: ${Package.price_per_weight(Package("", "", "", 15, ""))} per kg \n'
              f'Weight > 25 kg: ${Package.price_per_weight(Package("", "", "", 30, ""))} per kg \n'
              f'{"_" * 40} \n'
              f'Rates by collection point: \n'
              f'Home Delivery: ${Package.price_by_collect(Package("", "", "", "", "Home Collection"))} \n'
              f'Collection Center: ${Package.price_by_collect(Package("", "", "", "", "Collection center"))} \n'
              f'{"_" * 40} \n'
              f'THANK YOU FOR CHOOSING OUR PLATFORM!'
              )

    def type_price(self):
        if self.ship_type == "International":
            return [45, 20, 15]
        else:
            return [35, 10, 5]

    def method_price(self):
        if self.method == "Air":
            return 30
        else:
            return 10

    def tracking(self):
        pass


class Package(Shipping):
    def __init__(self, ship_type, method, size, weight, collect_type):
        super().__init__(ship_type, method)
        self.size = size
        self.weight = weight
        self.collect_type = collect_type

    @classmethod
    def get_package_detail(cls):
        ship_detail = Shipping.get_shipping_req()
        ship_type = ship_detail.ship_type
        method = ship_detail.method
        print(f'{"-" * 15}Insert Package Details{"-" * 15} \n')
        size = only1or2("Please choose the size of your package: \n"
                        "1 for small (< 1m) or 2 for large (>1m)", "Small",
                        "Large")
        weight = None
        while True:
            try:
                weight = int(input('Weight (in Kg):'))
                print(f'{"_" * 30} \n'
                      f'Total weight: {weight} kgs \n'
                      f'{"_" * 30} \n')
                break
            except ValueError:
                print("Invalid Entry! Please enter again :)")
                continue

        collect_type = only1or2("Point of Collection: \n"
                                "Choose 1 for Home Delivery(extra charges applied) \n"
                                "Choose 2 to collect from a Collection Center \n"
                                "", "Home Collection", "Collection Centre")
        return cls(ship_type, method, size, weight, collect_type)

    def price_by_size(self):
        if self.size == "Small":
            return 10
        else:
            return 25

    def price_per_weight(self):
        if self.weight <= 10:
            return 1.5
        elif 10 < self.weight <= 25:
            return 2.5
        else:
            return 3

    def price_by_collect(self):
        if self.collect_type == "Home Collection":
            return 5
        else:
            return 0

    def get_attributes(self):
        return [self.ship_type, self.method, self.size, self.weight, self.collect_type]


class Card:
    def __init__(self, card_num, expiry, holder_name, balance):
        self.card_num = card_num
        self.expiry = expiry
        self.holder_name = holder_name
        self.balance = balance

    # Just practising @property, getter and setter functions for instances.
    @property
    def card_num(self):
        return self.card_num

    @card_num.setter
    def card_num(self, value):
        if type(value) is not int:
            raise ValueError('Please enter a numeric value.')
        elif len(str(value)) != 16:
            raise ValueError("Please enter a 16 digit card number.")

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

                        print(f'Your card details are as follows:\n'
                              f'{"-" * 35} \n'
                              f'Card Number:{card_num} \n'
                              f'Expiry date: {expiry.strftime("%m/%y")} \n'
                              f'Card Holder Name: {holder_name} \n'
                              f'Card balance: ${"{:.2f}".format(balance)}')
                        return cls(card_num, expiry, holder_name, balance)
            except ValueError:
                print("Please enter a numeric value of 16 digit!")
                continue

    def get_card_info(self):
        return [self.holder_name, self.card_num, self.expiry, self.balance]


def start_program():
    print(f'{"_" * 60} \n'
          f'Hello, Thank you for choosing our shipping platform. \n'
          f'Please choose an option to continue: \n'
          f'[1] Check rates \n'
          f'[2] Obtain shipping cost estimate \n'
          f'{"_" * 60}')
    user_input = only1or2('', "Check rates", " Obtain Shipping Cost Estimate")
    if user_input == "Check rates":
        Shipping.check_rates()
    else:
        s1 = Package.get_package_detail()

        while True:
            print(f'Please verify your input: \n'
                  f'{"_" * 30} \n'
                  f'Shipping Type: {s1.get_attributes()[0]} \n'
                  f'Shipping Method: {s1.get_attributes()[1]}  \n'
                  f'Package Size: {s1.get_attributes()[2]} \n'
                  f'Package Weight: {s1.get_attributes()[3]} kg \n'
                  f'Collection Point: {s1.get_attributes()[4]} \n'
                  f'{"_" * 30}')
            verification = input('Is your input correct? Y/N')
            if verification.lower() == "y":
                priority_price = s1.price_by_size() + s1.price_by_collect() + s1.price_per_weight() * s1.weight + \
                                 s1.type_price()[0] + s1.method_price()
                express_price = s1.price_by_size() + s1.price_by_collect() + s1.price_per_weight() * s1.weight + \
                                s1.type_price()[1] + s1.method_price()
                standard_price = s1.price_by_size() + s1.price_by_collect() + s1.price_per_weight() * s1.weight + \
                                 s1.type_price()[2] + s1.method_price()
                print(f'\n'
                      f'You have the following shipping rate choices: \n'
                      f' [1] Priority Worldwide shipping (2-3 days): ${priority_price} \n'
                      f' [2] Express shipping (4-7 days): ${express_price} \n'
                      f' [3] Standard shipping (7-10 days): ${standard_price} \n')

                while True:
                    try:
                        after_verification = int(input('Please select among 1,2 or 3 for your choice of shipping:'))
                        if after_verification not in (1, 2, 3):
                            print('Please enter a valid choice!')
                            continue
                        elif after_verification == 1:
                            chosen_price = priority_price
                            break
                        elif after_verification == 2:
                            chosen_price = express_price
                            break
                        else:
                            chosen_price = standard_price
                            break
                    except ValueError:
                        print('Please enter a valid choice!')

                payment_type = only1or2("Would you like to pay by cash or card? \n"
                                        "Choose 1 for cash or 2 for card:", "cash", "card")
                if payment_type == "Cash":
                    print("Thank you for choosing our platform")

            elif verification.lower() == "n":
                while True:
                    wrong_input = input("Would you like to restart? Y/N")
                    if wrong_input.lower() == "y":
                        print('')
                        s1 = Package.get_package_detail()
                        break
                    elif wrong_input.lower() == "n":
                        print('Thank you for choosing this program. Please visit again!')
                        break
                    else:
                        print('Invalid Entry!')
                        continue
                if wrong_input.lower() == "n":
                    break
            else:
                print("Invalid Entry!")
                continue


card1 = Card.card_input()
