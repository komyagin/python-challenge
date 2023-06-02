from prettytable import PrettyTable
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        table = PrettyTable()
        table.field_names = ["Name", "Resource", "Measure"]
        table.add_row(["Water", self.resources['water'], 'ml'])
        table.add_row(["Milk", self.resources['milk'], "ml"])
        table.add_row(["Coffee", self.resources['coffee'],"g"])
        table.align = "l"
        print(table)

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
