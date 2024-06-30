# DSC 510
# Week 11
# Programming Assignment 11.1
# Author: Madhuri Basava
# 11/13/2022

import locale


# class used to calculate total price and number of items
class CashRegister:
    def __init__(self, total_price, item_count):
        self.total_price = total_price
        self.item_count = item_count

    def __repr__(self):
        pass

    def __str(self):
        pass

    def addItem(self, price):  # function returns the price
        self.total_price = self.total_price + price
        self.item_count = self.item_count + 1
        return self.total_price

    def pretty_print(self):
        print("*" * 35)
        print("Number of items: {}".format(self.getCount()))
        # print using locale.setlocale and locale.currency
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        total_price = locale.currency(self.getTotal(), grouping=True)
        print("Total Price:  {}".format(total_price))
        print("*" * 35)

    def getCount(self):
        return self.item_count

    def getTotal(self):
        return self.total_price


''' main() function definition '''


def main():
    print("Welcome Professor Michael Eller")

    # attribute initialization
    price = 0
    count = 0

    # creating an instance of class CashRegister
    cash = CashRegister(price, count)

    # Loop to enter the item price till the user doesn't wish to do it.
    while True:
        item = input("Do you want to add items to the cart enter 'Y' or 'N': ")
        if item.upper() == 'Y':
            try:
                price = float(
                    input("Please enter the item price: "))
            except ValueError as e:
                print("Please enter a number for price")
                continue
            cash.addItem(price)  # calling addItem() method to calculate the
            # total price

            cash.pretty_print()  # calling pretty_print() function to print
            # the total price snf item count in correct format

        elif item.upper() == 'N':
            break
        else:
            print("Please enter either 'Y' or 'N'")
            continue


''' calling main() function  '''

if __name__ == "__main__":
    main()
