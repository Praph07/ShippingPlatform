from extra import only1or2


class ShippingMethod:

    def __init__(self, method):
        self.method = method

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        if method not in ("Air", "Surface"):
            raise ValueError("Shipping method can only be Air or Surface")
        self._method = method

    def method_price(self):
        if self._method == "Air":
            return 5
        elif self._method == "Surface":
            return [3.5, 2.5]

    @classmethod
    def input_method(cls):
        input_method = only1or2("Choose your shipping method: \n"
                                "[1] Air \n"
                                "[2] Surface \n", "Air", "Surface")
        return cls(input_method)
