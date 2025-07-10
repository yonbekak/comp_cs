def display_menu(menu):
    for idx, item in enumerate(menu,1):
        print(f"{idx}. {item["name"]} -- ${item["base_price"]}")


def get_size_price(base_price, size):
    size_modifiers={
        "small" : 0.9,
        "medium" : 1.0,
        "large" : 1.2,
    }
    return base_price * size_modifiers[size]

def calculate_total(pizza):
    total = pizza["price"]
    # for topping in toppings:
    #     total += topping["price"]
    return total

menu = [
    {"name" : "Margharita","base_price": 10.99,},
    {"name": "Pepperoni","base_price": 12.99,}
]

current_order = {
    "pizza": None,
    "size": None,
    "total": 0.0,
}

display_menu(menu)
selection = int(input("Choose a pizza (1-2): ")) -1
current_order["pizza"]= menu[selection]

size=input("Choose size (small/medium/large): ")
current_order["price"] = get_size_price(menu[selection]["base_price"], size)

print(f"Your total is : ${calculate_total(current_order):.2f}")


