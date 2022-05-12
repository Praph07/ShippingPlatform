# here I import the module that implements regular expressions
import re


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


price_list = {"Shipping Category": {"International": {"Priority": 25, "Express": 15, "Standard": 10},
                                    "Local": {"Priority": 20, "Express": 10, "Standard": 5}},
              "Shipping Method": {"International": {"Air": 5, "Surface": 3.5}, "Local": {"Surface": 2.5}},
              "Package": {"Size": {"Small": 10, "Large": 15}, "Weight": {"<10": 1.5, ">=10 and <=25": 2.5, ">25": 3.5}},
              "Collection Point": {"Home": 2.5, "Collection Center": 0}}

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def test_email(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False
