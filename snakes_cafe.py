welcome_msg = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""
order_msg = """***********************************
** What would you like to order? **
***********************************"""

menu = {
    "Appetizers": {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0
    },
    "Entrees": {
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A Literal Garden": 0
    },
    "Desserts": {
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0
    },
    "Drinks": {
        
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }
}

def print_menu():
    print(welcome_msg)
    for category, items in menu.items():
        print(category)
        print("-------")
        for item in items:
            print(item)
        print()    
        

def order():
    print()

    order = input(">   ")
    if order == "quit":
        print_order(menu)
        print("Thank you for visiting Snakes Cafe!")
        print()
        exit()
    else:
        for _, items in menu.items():
            if order in items:
                items[order] += 1
                print(f"** {items[order]} order of {order} have been added to your meal **")
                return order

        print("Sorry, we don't have that item.")
        return order

def print_order(order):
    print()
    print("****************")
    print("** Your Order **")
    print("****************")
    
    for _, items in order.items():
        for item in items:
            if items[item] > 0:
                print(f"{items[item]} order of {item}")
            else:
                continue

def main():
    print_menu()
    
    print(order_msg)
    order()
    while True:
        order()

main()
