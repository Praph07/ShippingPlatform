from extra import only1or2


class ShippingCategory:

    def __init__(self, category):
        self.category = category

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in ("International", "Local"):
            raise ValueError("Shipping Category can only be International or Local")
        self._category = value

    def category_price(self):
        if self.category == "International":
            return [25, 15, 10]
        else:
            return [20, 10, 5]

    @classmethod
    def input_category(cls):
        input_category = only1or2("Where are you shipping your package: \n"
                                  "Internationally or Locally? \n"
                                  "Choose 1 for International and 2 for Local",
                                  "International", "Local")
        return cls(input_category)
