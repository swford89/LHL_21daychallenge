# Cleaning Supplies List (19 items)
cleaningsupplies_list = ['Broom', 'Mop', 'Dustpan', 'Garbage Bags', 'Glass Cleaner', 'Vinegar',
                        'Soap', 'Bleach', 'Duster', 'Floor Cleaner', 'Sponges', 'Dish Soap',
                        'Drain Cleaner', 'Paper Towels', 'Cleaning Rags', 'Toilet Cleaner', 
                        'Rubber Gloves', 'Alcohol Wipes', 'Squeegee']

# City Price
city_price = [6.49, 4.99, 3.39, 4.29, 3.99, 1.99, 
              1.50, 3.99, 4.99, 5.99, 2.99, 2.99, 
              5.99, 2.99, 3.49, 6.99, 2.99, 1.98, 11.99]

# Country Price
country_price = [5.49, 4.69, 4.42, 5.99, 5.99, 2.50,
                1.25, 2.49, 4.50, 6.75, 2.49, 1.99, 
                6.25, 3.99, 3.59, 4.99, 1.69, 1.87, 10.99]

# which items cost 10% more in the town?
# make a list of these items

values_list = list(zip(city_price, country_price))
city_country = dict(zip(cleaningsupplies_list, values_list))

for key, value in city_country.items():
    city, country = value
    if city < country:
        diff = country - city
        print(f"The country price for {key} is ${diff: .2f} more than the city price.")
        percent_diff = diff / country
        if percent_diff >= 0.10:
            print(key)
            print(f"{key} = {percent_diff * 100: .2f}% more than the city price")

# Dustpan ========= +23.30%
# Garbage Bags ==== +28.38%
# Glass Cleaner === +33.39%
# Vinegar ========= +20.40%
# Floor Cleaner === +11.26%
# Paper Towels ==== +25.06% 