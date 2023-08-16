from data import MENU

def calculate_coin_value(quarters, dimes, nickels, pennies):
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    total_value = (quarters * quarter_value) + (dimes * dime_value) + (nickels * nickel_value) + (pennies * penny_value)
    return total_value


user_choice = True
water = 300
milk = 200
coffee = 100
money = 0

while user_choice:

    user = input("What would you like? (espresso/latte/cappuccino:)").lower()
    if user == "off":
        user_choice = False
    elif user == "report":
        print(f"Water:{water}ml \nMilk:{milk}ml \nCoffee:{coffee}g \nMoney:${money}")
    elif user in MENU:
        coffee_type = MENU[user]
        coffee_cost = coffee_type["cost"]
        required_water = coffee_type['ingredients']['water']
        required_milk = coffee_type['ingredients'].get('milk', 0)
        required_coffee = coffee_type['ingredients'].get('coffee', 0)
        if water < required_water:
            print("Sorry, there is not enough water.")
        elif milk < required_milk:
            print("Sorry, there is not enough milk.")
        elif coffee < required_coffee:
            print("Sorry, there is not enough coffee.")
        else:
            # Get user input for each coin type
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))

            total_value = calculate_coin_value(quarters, dimes, nickels, pennies)
            if total_value >= coffee_cost:
                change = total_value - coffee_cost
                print(f"Here is ${change:.2f} in change")
                print(f"Here is your {user}☕. Enjoy!")
                money += coffee_cost
                water -= required_water
                milk -= required_milk
                coffee -= required_coffee
            else:
                print("Sorry that's not enough money. Money refunded.")


