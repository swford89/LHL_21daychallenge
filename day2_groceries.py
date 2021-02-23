# for loop 
# basic math operations

# Grocery List (19 items)
grocery_list = ['Bananas', 'Clementines', 'Baguette', 'Oat Milk', 'Olive Oil', 'Coffee Beans',
                'Chocolate Bar', 'Brocolli', 'Eggplant', 'Chickpeas', 'Lentils', 'Tomatoes',
                'Pasta', 'Rice', 'Yogurt', 'Blueberries', 'Onions', 'Garlic', 'Truffles']

# City Price
city_price = [6.49, 4.99, 4.39, 4.29, 11.99, 17.99,          
              3.49, 3.99, 1.10, 1.99, 2.99, 4.68,            
              1.59, 8.99, 3.49, 6.99, 2.99, 1.98, 14.99]

# Country Price
country_price = [4.49, 4.12, 3.42, 6.99, 7.99, 14.99,              
                2.99, 2.49, 0.99, 1.49, 2.49, 1.99,              
                1.59, 6.99, 3.89, 4.99, 1.69, 1.87, 11.49]


city_sum = 0
country_sum = 0

for price in range(len(city_price)):
    city_sum += city_price[price]

for price in range(len(country_price)):
    country_sum += country_price[price]

print(f"The grocery total for the city is: {city_sum: .2f}.")
print(f"The grocery total for the country is: {country_sum}.")

price_diff = city_sum - country_sum
print(f"The price difference between the two is: {price_diff: .2f}.")

percent_diff_country = price_diff / country_sum
print(f"The difference between the two, as a percentage of the country prices is: {percent_diff_country: .4f}")
