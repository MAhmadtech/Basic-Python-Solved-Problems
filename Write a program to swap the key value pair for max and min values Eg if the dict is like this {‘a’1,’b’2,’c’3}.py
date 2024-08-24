

# Write a program to swap the key value pair for max and min values
# Eg if the dict is like this {‘a’:1,’b’:2,’c’:3}
# Output should be {a:3,b:2,c:1}

my_dict = {'a': 1, 'b': 2, 'c': 3}
max_value = max(my_dict.values())  
min_value = min(my_dict.values())  
max_key = [key for key, value in my_dict.items() if value == max_value][0]  
min_key = [key for key, value in my_dict.items() if value == min_value][0]  
del my_dict[max_key]
del my_dict[min_key]  
my_dict[max_key] = min_value 
my_dict[min_key] = max_value  
print(my_dict)  

