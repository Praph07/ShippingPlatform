print("Hello, Thank you for choosing our shipping platform.")
print("Please follow along to obtain to shipping cost estimate:")

class Shipping:
    def __init__(self, ship_type, method):
        self.ship_type = ship_type
        self.method = method

    def __str__(self):
        return 'Chosen shipping type and method: ' + self.ship_type + ',' + self.method

    def get_method(self):
        return self.method

    def get_shipping_req():
        return cls(
            input("Where are you shipping? International or local?"),
            input("Are do you want to ship by air or surface?")
        )


print("Where are you shipping your package: Internationally or Locally? "
      "Choose 1 for international and 2 for Local.")
while True:
    ship_choice = int(input('Please choose between 1 or 2:'))
    if ship_choice not in (1, 2):
        print('Please choose a correct value!')
    elif ship_choice == 1:
        ship_type = "International"
        print("You have chosen International shipping. You have two options for Shipping Method:")
        print('Air Shipping and Surface Shipping. Choose 1 For Air and 2 For Surface shipping');
        while True:
            ship_method_choice = int(input("Please Choose Shipping method for your International Shipping:"))
            if ship_method_choice not in (1, 2):
                print('Invalid Choice!')
            elif ship_method_choice == 1:
                ship_method = "Air"
                break
            else:
                ship_method = "Surface"
                break
        break
    else:
        ship_type = "Local"
        ship_method = "Air"
        break

s1 = Shipping(ship_type, ship_method)
print(s1.__str__())


class Package(Shipping):
    def __init__(self, ship_type, method, size, weight):
        super().__init__(ship_type, method)
        self.size = size
        self.weight = weight

