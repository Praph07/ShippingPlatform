from extra import only1or2, price_list
from shipping import Shipping
from card import Card


def start_program():
    print(f'{"_" * 60} \n'
          f'Hello, Thank you for choosing our shipping platform. \n'
          f'Please choose an option to continue: \n'
          f'[1] Check rates \n'
          f'[2] Obtain shipping cost estimate and process shipping \n'
          f'{"_" * 60}')
    user_input = only1or2('', "Check rates", " Obtain Shipping Cost Estimate")
    if user_input == "Check rates":
        print(f'{"*" * 40} \n'
              f'The flat shipping rates are as follows: \n'
              f'{"*" * 40} \n'
              f'\n'
              f'Rates by shipping type: \n'
              f'\n'
              f'International Shipping: \n'
              f'{"_" * 40} \n'
              f'Priority Worldwide '
              f'Shipping(2-3 days): ${price_list["Shipping Category"]["International"]["Priority"]} \n'
              f'Express International '
              f'Shipping(4-7 days): ${price_list["Shipping Category"]["International"]["Express"]} \n'
              f'Standard Shipping(7-10 days): ${price_list["Shipping Category"]["International"]["Standard"]} \n'
              f'International Surface Shipping: ${price_list["Shipping Method"]["International"]["Surface"]} \n'
              f'International Air Shipping: ${price_list["Shipping Method"]["International"]["Air"]} \n'
              f'\n'
              f'Local Shipping: \n'
              f'{"_" * 40} \n'
              f'Priority Local Shipping(2-3 days): ${price_list["Shipping Category"]["Local"]["Priority"]} \n'
              f'Express Local Shipping(4-7 days): ${price_list["Shipping Category"]["Local"]["Express"]} \n'
              f'Standard Local Shipping(7-10 days): ${price_list["Shipping Category"]["Local"]["Standard"]} \n'
              f'Surface Shipping: ${price_list["Shipping Method"]["Local"]["Surface"]} \n'
              f'{"_" * 40} \n'
              f'\n'
              f'Rates by package size: \n'
              f'{"_" * 40} \n'
              f'Small Packages (<1 cubic meter): ${price_list["Package"]["Size"]["Small"]} \n'
              f'Large Packages (>1 cubic meter): ${price_list["Package"]["Size"]["Large"]} \n'
              f'{"_" * 40} \n'
              f'Rates by package weight: \n'
              f'{"_" * 40} \n'
              f'Weight <= 10 kg: ${price_list["Package"]["Weight"]["<10"]} per kg \n'
              f'Weight between 10 to 25 kg: ${price_list["Package"]["Weight"][">=10 and <=25"]} per kg \n'
              f'Weight > 25 kg: ${price_list["Package"]["Weight"][">25"]} per kg \n'
              f'{"_" * 40} \n'
              f'Rates by collection point: \n'
              f'{"_" * 40} \n'
              f'Home Delivery: ${price_list["Collection Point"]["Home"]} \n'
              f'Collection Center: ${price_list["Collection Point"]["Collection Center"]} \n'
              f'{"_" * 40} \n'
              f'THANK YOU FOR CHOOSING OUR PLATFORM!'
              )
    else:
        invalid_card_choice = ''
        while True:
            shipping = Shipping.get_shipping_req()
            payment_type = only1or2("Would you like to pay by cash or card? \n"
                                    "Choose 1 for cash or 2 for card:", "Cash", "Card")
            if payment_type == "Cash":
                print(f'Please verify your shipping details: \n'
                      f'{"_" * 30} \n'
                      f'Shipping Category: {shipping.category.category} \n'
                      f'Shipping Method: {shipping.method.method}  \n'
                      f'Package Length: {shipping.package.length} \n'
                      f'Package Width: {shipping.package.width} \n'
                      f'Package Height: {shipping.package.height} \n'
                      f'Calculated Package Size: {shipping.package.size} \n'
                      f'Package Weight: {shipping.package.weight} kg \n'
                      f'Chosen Shipping Option: {shipping.speed} \n'
                      f'Total shipping cost: {shipping.price} \n'
                      f'{"_" * 30}')
                verification = input('Do you verify your shipping details and confirm payment? (y/n))')
                if verification.lower() == "y":
                    print("\nObtaining your Shipping tracking number...\n")
                    print(f'Please show this tracking number during pickup: {shipping.tracking}\n')
                    print(shipping)
                    print('Thank you for choosing our platform.\n')
                    break
                elif verification.lower() == "n":

                    terminate_or_restart = only1or2("Would you like to restart or terminate the program? \n"
                                                    "[1] Restart \n"
                                                    "[2] Terminate \n", "Restart", "Terminate")
                    if terminate_or_restart == "Restart":
                        print('')
                        continue
                    elif terminate_or_restart == "n":
                        print('Thank you for choosing this program. Please visit again!')
                        break
                break
            else:
                while True:
                    card_details = Card.card_input()

                    if card_details.balance < shipping.price:
                        invalid_card_choice = only1or2(
                            "You have entered a card with insufficient balance for payment! Would you like to enter "
                            "another card or pay by cash? \n [1] Cash \n [2] Card \n",
                            "Cash", "Card")
                        if invalid_card_choice == "Card":
                            continue
                        else:
                            break
                    else:
                        break
            if invalid_card_choice == "Cash":
                print(f'Please verify your input: \n'
                      f'{"_" * 30} \n'
                      f'Shipping Category: {shipping.category.category} \n'
                      f'Shipping Method: {shipping.method.method}  \n'
                      f'Package Length: {shipping.package.length} \n'
                      f'Package Width: {shipping.package.width} \n'
                      f'Package Height: {shipping.package.height} \n'
                      f'Calculated Package Size: {shipping.package.size} \n'
                      f'Package Weight: {shipping.package.weight} kg \n'
                      f'Chosen Shipping Option: {shipping.speed} \n'
                      f'Total shipping cost: {shipping.price} \n'
                      f'{"_" * 30}')
                verification = input('Do you verify your shipping details and confirm payment? (y/n))')
                if verification.lower() == "y":
                    print("\nObtaining your Shipping tracking number...\n")
                    print(f'Please show this tracking number during pickup: {shipping.tracking}\n')
                    print(shipping)
                    print('Thank you for choosing our platform.\n')
                    break
                elif verification.lower() == "n":

                    terminate_or_restart = only1or2("Would you like to restart or terminate the program? \n"
                                                    "[1] Restart \n"
                                                    "[2] Terminate \n", "Restart", "Terminate")
                    if terminate_or_restart == "Restart":
                        print('')
                        continue
                    elif terminate_or_restart == "n":
                        print('Thank you for choosing this program. Please visit again!')
                        break
                break
            else:
                print(f'Please verify your input: \n'
                      f'{"_" * 30} \n'
                      f'Shipping Category: {shipping.category.category} \n'
                      f'Shipping Method: {shipping.method.method}  \n'
                      f'Package Length: {shipping.package.length} \n'
                      f'Package Width: {shipping.package.width} \n'
                      f'Package Height: {shipping.package.height} \n'
                      f'Calculated Package Size: {shipping.package.size} \n'
                      f'Package Weight: {shipping.package.weight} kg \n'
                      f'Chosen Shipping Option: {shipping.speed} \n'
                      f'Total shipping cost: {shipping.price} \n'
                      f'{"_" * 30}')
                verification = input('Do you verify your shipping details and confirm payment? (y/n))')
                if verification.lower() == "y":
                    print("\nConfirming payment and obtaining tracking number...\n")
                    print(f'PAYMENT SUCCESSFUL! \n'
                          f'Your new balance is {card_details.deduce_balance(shipping.price)}\n')
                    print(shipping)
                    print('Thank you for choosing our platform.\n'
                          )
                    break
                elif verification.lower() == "n":

                    terminate_or_restart = only1or2("Would you like to restart or terminate the program? \n"
                                                    "[1] Restart \n"
                                                    "[2] Terminate \n", "Restart", "Terminate")
                    if terminate_or_restart == "Restart":
                        print('')
                        continue
                    elif terminate_or_restart == "Terminate":
                        print('Thank you for choosing this program. Please visit again!')
                        break


start_program()
