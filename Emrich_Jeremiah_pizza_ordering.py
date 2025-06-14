# Create a function to display menu items.
def welcome():
    print("Welcome to Emrich's pizza")
    print ("Menu:")
    print("1. Small cheese pizza - 12.00")
    print("2. Medium cheese pizza - 14.00")
    print("3. Large cheese pizza - 16.00")

# Get users input.
def get_choices():
    base_price = 0 # Base price of 0 and add as the user adds item to their pizza
    choice = input("Enter what which size pizza you would like. (1- small, 2- medium, 3- large): ")
    if choice == "1":
        base_price += 12.00 # Add 12.00 if small cheese pizza is selected.
        size = "small"
        print("small pizza added. $12.00")
    elif choice == "2":
        base_price += 14.00 # Add 14.00 if small cheese pizza is selected.
        size = "medium"
        print("medium pizza added. $14.00")
    elif choice == "3":
        base_price += 16.00 # Add 16.00 if small cheese pizza is selected.
        size = "large"
        print("large pizza added. $16.00")
# Give the user the option to add toppings for additional 1.50 per topping.
    add_pepperoni = input("Would you like to add pepperoni? 1 = yes, 0 = no: ")
    if add_pepperoni == "1":
        base_price += 1.50 # Add 1.50 if pepperoni is added.
        print("Pepperoni added. Add $1.50")
    add_sausage = input("Would you like to add sausage? 1 = yes, 0 = no: ")
    if add_sausage == "1":
        base_price += 1.50 # Add 1.50 if sausage is added.
        print("Sausage added. Add 1.50")
    add_olives = input("Would you like to add olives? 1 = yes, 0 = no: ")
    if add_olives == "1":
        base_price += 1.50 # Add 1.50 if olives are added.
        print("Olives added. Add $1.50")
# Get quantity from the user.
    qty = input("How many pizzas would you like? ")
# calculate the total price of the base price and additions times quantity.
    order_total = float(qty) * base_price

# Display to the user how many pizzas were ordered and the total price.
    print(f"Your order total for {qty} {size} pizzas is ${order_total:.2f} ")



if __name__ == "__main__":
    welcome()
    get_choices()