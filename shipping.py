from extra import only1or2
from package import Package
from shippingcategory import ShippingCategory
from shippingmethod import ShippingMethod
from user import *
import random


class Shipping:
    def __init__(self, category, method, sender, receiver, package, speed, collection, price, tracking):
        self.category = category
        self.method = method
        self.sender = sender
        self.receiver = receiver
        self.package = package
        self.speed = speed
        self.collection = collection
        self.price = price
        self.tracking = tracking

    @classmethod
    def get_shipping_req(cls):
        print(f'Enter your contact and address details:\n'
              f'{"_" * 30} \n')
        sender = Sender.get_user_detail()
        print("")
        chosen_category = ShippingCategory.input_category()
        chosen_method = ''
        if chosen_category.category == "International":
            print('For international Shipping, there are two shipping methods.')
            chosen_method = ShippingMethod.input_method()
            if chosen_method.method == "Air":
                ship_method_price = chosen_method.method_price()
            else:
                ship_method_price = chosen_method.method_price()[0]
        else:
            ship_method = ShippingMethod("Surface")
            print("Your method of shipping will be via Surface shipping. \n")
            ship_method_price = ship_method.method_price()[1]
        package = Package.get_package_detail()
        print(f'Enter receiver contact and address details:\n'
              f'{"_" * 30} \n')
        receiver = Receiver.get_user_detail()
        collection = only1or2(f"\n Please choose a collection point for this delivery: \n"
                              f"[1] Home Delivery \n"
                              f"[2] Collection center at {receiver.address} \n", "Home Delivery", "Collection Center")
        collection_price = 0
        if collection == "Home Delivery":
            print("There is a 5 dollar charge for home delivery! ")
            # add do you accept this?
            collection_price = 5
        priority_price = package.price_by_size() + package.price_per_weight() + ship_method_price + \
                         chosen_category.category_price()[0] + collection_price
        express_price = package.price_by_size() + package.price_per_weight() + ship_method_price + \
                        chosen_category.category_price()[1] + collection_price
        standard_price = package.price_by_size() + package.price_per_weight() + ship_method_price + \
                         chosen_category.category_price()[2] + collection_price
        print(f'\n'
              f'You have the following shipping rate choices: \n'
              f' [1] Priority Worldwide shipping (2-3 days): ${priority_price} \n'
              f' [2] Express shipping (4-7 days): ${express_price} \n'
              f' [3] Standard shipping (7-10 days): ${standard_price} \n')

        while True:
            try:
                chosen_ship_speed = ""
                chosen_price = 0
                after_verification = int(input('Please select among 1,2 or 3 for your choice of shipping:'))
                if after_verification not in (1, 2, 3):
                    print('Please enter a valid choice!')
                    continue
                elif after_verification == 1:
                    chosen_ship_speed = "Priority WorldWide (2-3) days"
                    chosen_price = priority_price
                    print(f'{"_" * 30} \n'
                          f'You have chosen: Priority Worldwide shipping (2-3 days) \n'
                          f'Your total cost will be {chosen_price}$ \n'
                          f'{"_" * 30} \n')
                    break
                elif after_verification == 2:
                    chosen_ship_speed = "Express shipping (4-7 days)"

                    chosen_price = express_price
                    print(f'{"_" * 30} \n'
                          f'You have chosen: Standard shipping (7-10 days) \n'
                          f'Your total cost will be {chosen_price}$ \n'
                          f'{"_" * 30} \n')
                    break
                else:
                    chosen_ship_speed = "Priority WorldWide (2-3) days"
                    chosen_price = standard_price
                    print(f'{"_" * 30} \n'
                          f'You have chosen: Standard shipping (7-10 days) \n'
                          f'Your total cost will be {chosen_price}$ \n'
                          f'{"_" * 30} \n')
                    break
            except ValueError:
                print('Please enter a valid choice!')
        tracking = random.randint(1000000000, 1999999999)

        return cls(chosen_category, chosen_method, sender, receiver, package, chosen_ship_speed, collection,
                   chosen_price, tracking)

    def __str__(self):
        return f'Your Shipping order details are as follows:\n' \
               f'{"_" * 30} \n' \
               f'Sender Details: \n' \
               f'{"_" * 30} \n' \
               f'First Name: {self.sender.firstname}\n' \
               f'Last Name: {self.sender.lastname}\n' \
               f'Email: {self.sender.email}\n' \
               f'Address: {self.sender.address}\n'\
               f'{"_" * 30} \n' \
               f'Receiver Details: \n' \
               f'{"_" * 30} \n' \
               f'First Name: {self.receiver.firstname}\n' \
               f'Last Name: {self.receiver.lastname}\n' \
               f'Email: {self.receiver.email}\n' \
               f'Address: {self.receiver.address}\n' \
               f'{"_" * 30} \n' \
               f'Package Details: \n' \
               f'{"_" * 30} \n' \
               f'Shipping Category: {self.category.category} \n'\
               f'Shipping Method: {self.method.method}  \n'\
               f'Package Length: {self.package.length} \n'\
               f'Package Width: {self.package.width} \n'\
               f'Package Height: {self.package.height} \n'\
               f'Calculated Package Size: {self.package.size} \n'\
               f'Package Weight: {self.package.weight} kg \n'\
               f'Chosen Shipping Option: {self.speed} \n'\
               f'Total shipping cost: {self.price} \n'\
               f'{"_" * 30} \n'\
               f'Shipping Details:\n'\
               f'{"_" * 30}\n' \
               f'Shipping Speed: {self.collection}\n' \
               f'Total Cost: ${self.price}\n' \
               f'Tracking number: {self.tracking}\n'\
               f'{"_" * 30} \n'
