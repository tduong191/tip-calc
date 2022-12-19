
# create a person class
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.orders = []
        self.percentage = 0
        self.tax = 0
        self.tip = 0
        self.total = 0
    
    # get the total
    def get_total(self):
        return self.total
    
    # set the total
    def set_total(self, total):
        self.total = total


    # get the tax
    def get_tax(self):
        return self.tax
    
    # set the tax
    def set_tax(self, tax):
        self.tax = tax
    
    # get the tip
    def get_tip(self):
        return self.tip
    
    # set the tip
    def set_tip(self, tip):
        self.tip = tip


    # get the name
    def get_name(self):
        return self.name

    # get the orders
    def get_orders(self):
        return self.orders

    # set the name
    def set_name(self, name):
        self.name = name

    # add an order
    def add_order(self, order):
        self.orders.append(order)

    # get the total
    def get_before_tax(self):
        before_tax = 0
        for order in self.orders:
            before_tax += order.get_total()
        return before_tax
    
    # get the percentage
    def get_percentage(self):
        return self.percentage
    
    # set the percentage
    def set_percentage(self, percentage):
        self.percentage = percentage

# create an order class
class Order:
    # constructor
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # get the name
    def get_name(self):
        return self.name

    # get the price
    def get_price(self):
        return self.price

    # get the quantity
    def get_quantity(self):
        return self.quantity

    # get the total
    def get_total(self):
        return self.price * self.quantity


# main function
def main():
    # get the number of people
    people = int(input("Enter the number of people: "))
    print()
    # create a list of people
    person_list = []
    # loop through the people
    for i in range(people):
        # get the name
        name = input("Enter the name: ")
        # create a person
        person = Person(name, 0)
        # get the number of orders
        orders = int(input("Enter the number of orders: "))
        # loop through the orders
        for j in range(orders):
            # get the order name
            order_name = input("Enter the order name: ")
            # get the order price
            order_price = float(input("Enter the order price: "))
            # get the order quantity
            order_quantity = int(input("Enter the order quantity: "))
            # create an order
            order = Order(order_name, order_price, order_quantity)
            # add the order to the person
            person.add_order(order)
        # add the person to the list
        person_list.append(person)
        print()
    
    # enter the tax amount
    tax = float(input("Enter the tax amount: "))
    # enter the tip percentage
    tip = float(input("Enter the tip percentage: "))
    print() 
    # get the before tax total
    before_tax = 0
    for person in person_list:
        before_tax += person.get_before_tax()
    # calculate the tip
    tip_amount = (before_tax + tax) * (tip / 100)
    # calculate the total
    total = before_tax + tax + tip_amount
    # calculate the percentage for each person
    for person in person_list:
        person.set_percentage(person.get_before_tax() / before_tax)
        # calculate the tax for each person
        person.set_tax(person.get_percentage() * tax)
        # calculate the tip for each person
        person.set_tip(person.get_percentage() * tip_amount)
        # calculate the total for each person
        person.set_total(person.get_before_tax() + person.get_tax() + person.get_tip())
    
    # display the order for each person and price, the tax, the tip, and the total
    for person in person_list:
        print(person.get_name())
        print("Orders:")
        for order in person.get_orders():
            print(order.get_name(), " x ", order.get_quantity(), ": $", format(order.get_total(), ".2f"), sep="")
        print("Tax: $", format(person.get_tax(), ".2f"), sep="")
        print("Tip: $", format(person.get_tip(), ".2f"), sep="")
        print("Total: $", format(person.get_total(), ".2f"), sep="")
        print()


    # display the tip amount, tax amount, and total
    print("Final Bill")
    print("Before tax and tip amount: $", format(before_tax, ".2f"), sep="")
    print("Tip amount: $", format(tip_amount, ".2f"), sep="")
    print("Tax amount: $", format(tax, ".2f"), sep="")
    print("Total: $", format(total, ".2f"), sep="")


# call the main function
main()

