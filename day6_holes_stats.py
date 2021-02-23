'''
import pandas as pd # we must import our external python plugin

list_of_num = [1,2,3,4,5]

series = pd.Series(list_of_num) #converting our list_of_num to a pandas series variable
                                #we need to do this to use some of pandas' useful descriptive statistics functions

series.max()    #outputs maximum value in Pandas Series
series.min()    #outputs minimum value in Pandas Series
series.mean()   #outputs average value in Pandas Series
series.median() #outputs median value in Pandas Series
series.mode()   #outputs mode value in Pandas Series
'''

### small (< 20mm) ================== $1.30
### medium (>= 20mm but < 70mm) ===== $1.60
### large (>= 70mm) ================= $2.10
# 
# Question 1: what is the average sized hole?
# Question 2: what is the average cost to fix a hole?
# Question 3: what is the total cost of fixing all of the holes?

import pandas as pd

import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

#print(hole_sizes[:])

series = pd.Series(hole_sizes)

print(f"{series.mean()} is the average size (sum divided by the total number).")
print(f"{series.max()} is the size of the largest hole.")
print(f"{series.min()} is the size of the smallest hole.")
print("")

small_count = 0
medium_count = 0
large_count = 0

for hole in hole_sizes:
    if hole < 20:
        small_count += 1 
    elif hole >= 20 and hole < 70:
        medium_count += 1
    elif hole >= 70:
        large_count += 1

small_cost = small_count * 1.30
medium_cost = medium_count * 1.60
large_cost = large_count * 2.10

total_cost = small_cost + medium_cost + large_cost

average_cost = total_cost / len(series)

print(f"The number of holes: {small_count}")
print(f"The cost to fix the small holes: {small_count * 1.30: .2f}")
print("")
print(f"The number of medium holes: {medium_count}")
print(f"The cost to fix the medium holes: {medium_count * 1.60: .2f}")
print("")
print(f"The number of large holes: {large_count}")
print(f"The cost to fix the large holes: {large_count * 2.10: .2f}")
print("")
print(f"The total cost to fix all the holes: {total_cost: .2f}")
print(f"The average cost to fix a hole is: {average_cost: .2f}")

# hole sizes in mm
hole_sizes[:5]