from datetime import datetime


def get_card_info():
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
                        print("Please enter with the correct date format (mm/yy)!")
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
                          f'{"-"*35} \n'
                          f'Card Number:{card_num} \n'
                          f'Expiry date: {expiry.strftime("%m/%y")} \n'
                          f'Card Holder Name: {holder_name} \n'
                          f'Card balance: ${"{:.2f}".format(balance)}')
                    break
        except ValueError:
            print("Please enter a numeric value of 16 digit!")
            continue


get_card_info()
