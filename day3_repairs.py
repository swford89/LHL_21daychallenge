# lists and dictionaries
# indexing

# hate oak, prefer maple
# paint all rooms BLUE, except the kitchen which they want to paint WHITE   

old_blueprint = {
    "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],                # WHITE PAINT
    "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],     # BLUE
    "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],              # BLUE
    "Bedroom" : ["Clean", 'Mahogany', 'Good Condition', 'Green'],   # BLUE
    "Bathroom": ["Dirty", 'White Tile', 'Good Condition','White'],  # BLUE
    "Shed"    : ['Dirty', "Cherry", "Damaged", "Un-painted"]        # NO PAINT      
}

shopping_list = ['20 x Oak Plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']
new_shopping_list = shopping_list.copy()

for item in new_shopping_list:
    if item == 'White Paint':
        item_index = new_shopping_list.index('White Paint')
        new_shopping_list[item_index] = 'Blue Paint'

    if item == 'Blue Paint':
        blue_count = new_shopping_list.count('Blue Paint')
        if blue_count < 4:
            new_shopping_list.append('Blue Paint')
    
    if new_shopping_list.count('White Paint') == 0:
        new_shopping_list.insert(3, 'White Paint')

    if item == '20 x Oak Plank':
        oak_index = new_shopping_list.index(item)
        new_shopping_list[oak_index] = '20 x Maple Plank'

paint_list = new_shopping_list[3:]
print(paint_list)
print(shopping_list)
print(new_shopping_list)

