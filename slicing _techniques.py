# Task 1: Given the list of temperatures:
# Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
# 83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 
                97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

segment = temperatures[7:14]
print(segment)

# Task 2: Extract all the temperatures above 100.

temperatures_above_100 = temperatures[:23]
print(temperatures_above_100)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.reverse()
print(temperatures)
reversed_list = [106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96,
                 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 75, 72]
reversed_segment = reversed_list[4:9]
print(reversed_segment)


