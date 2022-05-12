class Package:
    def __init__(self, width, length, height, weight, size):

        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.size = size

    @classmethod
    def get_package_detail(cls):
        while True:

            print(f'{"-" * 15}Insert Package Details{"-" * 15} \n')
            while True:
                try:
                    length = float(input("Length(in m):"))
                    if length <= 0:
                        print('Length cannot be negative! \n')
                        continue
                    else:
                        break
                except ValueError:
                    print("Please enter a valid length.\n")

            while True:
                try:
                    height = float(input("Height(in m):"))
                    if height <= 0:
                        print('Height cannot be negative!\n')
                        continue
                    else:
                        break
                except ValueError:
                    print("Please enter a valid height.\n")

            while True:
                try:
                    width = float(input("Width(in m):"))
                    if width <= 0:
                        print('Width cannot be negative!\n')
                        continue
                    else:
                        break
                except ValueError:
                    print("Please enter a valid Width.\n")

            weight = None
            while True:
                try:
                    weight = float(input('Weight (in Kg):'))
                    if weight <= 0:
                        print('Weight cannot be negative!\n')
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid Entry! Please enter again. \n")
                    continue

            if width * length * height <= 1:
                size = "Small"
            else:
                size = "Large"

            print(f'\n'
                  f'Your package details are as follows:\n'
                  f'{"*" * 25} \n'
                  f'Length: {length}m \n'
                  f'Height: {height}m \n'
                  f'Width: {width}m \n'
                  f'Weight: {weight} \n'
                  f'\n'
                  f'Based on your input, your package size falls on the {size} Category. \n')
            while True:
                package_verification = input('Do you verify your package input? (y/n) \n')
                if package_verification.lower() == "y":
                    print("Your package details have been confirmed! \n")
                    break
                elif package_verification.lower() == "n":
                    print("Please reenter your details! \n")
                    break
                else:
                    print("Invalid Choice! \n")
                    continue
            if package_verification.lower() == "n":
                continue
            else:
                return cls(height, length, width, weight, size)

    def price_per_weight(self):
        if self.weight <= 10:
            return 1.5*self.weight
        elif 10 < self.weight <= 25:
            return 2.5*self.weight
        else:
            return 3*self.weight

    def price_by_size(self):
        if self.size == "Small":
            return 5
        else:
            return 10


