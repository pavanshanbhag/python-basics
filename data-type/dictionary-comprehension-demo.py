#%%
"""
Template : dict_variable = { key:value for (key:value) in dictionary.items() }

Example 1 : Double the values of a dictionary
"""
dict_var1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dict_var1)

ex1 = {k:v**2 for (k,v) in dict_var1.items()}
print('Output of ex1  : ')
print(ex1)


#%%
'''
 create the same dictionary as above but also change the names of the key
'''
ex2 = {k*2 :v for (k,v) in dict_var1.items()}
print(ex2)

#%%
'''
example 3 :
create a new dictionary where the key is a number divisible by 2 in a range of 0-10 and it's value is the square of the number.
'''
numbers = range(10)
ex3 = { n:n**2 for n in numbers if n%2 == 0 }
print(ex3)

#%%
''''
Alternative to lambda function
'''
# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)

# Initialize the `fahrenheit` dictionary 
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)

#%%
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}

print(dict1_cond)

#%%
dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)

#%%
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}

print(dict1_tripleCond)

#%%
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}

print(dict1_tripleCond)

#%%
#nested dictionary comprehension
nested_dict = {'first':{'a':1}, 'second':{'b':2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)

#%%
