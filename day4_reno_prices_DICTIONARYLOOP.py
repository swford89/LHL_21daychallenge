item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600,150,15,165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]

# need 600 Oak Planks ----------------- wholesale = 7000.00 and retail per plank = 12.99
# need 150L of Blue Paint ------------- wholesale = 1000.00 and retail per liter = 8.99
# need 15L of White Paint ------------- wholesale = 1000.00 and retail per liter = 9.99
# need 165L of Paint Finish ----------- wholesale =  800.00 and retail per liter = 3.99

everything_dict = {
    'Oak': (600, 12.99),
    'Blue Paint': (150, 8.99),
    'White Paint': (15, 9.99),
    'Paint Finish': (165, 3.99),
}

for key, value in everything_dict.items():
    print(key, value)

print('')

for item, tuple_product in everything_dict.items():
    amount, price = tuple_product
    cost = amount * price
    print(f"The retail total for {item} is: {cost}")
