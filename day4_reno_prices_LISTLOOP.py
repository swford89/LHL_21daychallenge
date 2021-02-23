item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600,150,15,165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]

# need 600 Oak Planks ----------------- wholesale = 7000.00 and retail per plank = 12.99
# need 150L of Blue Paint ------------- wholesale = 1000.00 and retail per liter = 8.99
# need 15L of White Paint ------------- wholesale = 1000.00 and retail per liter = 9.99
# need 165L of Paint Finish ----------- wholesale =  800.00 and retail per liter = 3.99

retail_amount_list = [
    [amount_list[0], retail_price[0]], 
    [amount_list[1], retail_price[1]], 
    [amount_list[2], retail_price[2]],
    [amount_list[3], retail_price[3]],
]

for values in retail_amount_list:
    cost = values[0] * values[1]
    print(f"The total cost is {cost}, for {values[0]} at ${values[1]}")

# retail cost of 600 planks =========== 7,794.00 ------------------ ABOVE WHOLESALE
# retail cost of 150L of Blue Paint === 1,348.00 ------------------ ABOVE WHOLESALE

# retail cost of 15L of White Paint === 149.85 -------------------- below wholesale
# retail cost of 165L of Paint Finish = 658.35 -------------------- below wholesale
