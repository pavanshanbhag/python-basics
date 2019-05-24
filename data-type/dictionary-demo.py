#%%
#creating an empty dictionary
dict_var = {}
dict_var2 = dict()

print("Empty Dictionary: ") 
print(dict_var) 
  
# Adding elements one at a time 
dict_var[0] = 'Pavan'
dict_var[2] = 'Shanbhag'
dict_var[3] =  124
print("\nDictionary after adding 3 elements: ") 
print(dict_var) 
  
# Adding set of values  
# to a single Key 
dict_var['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(dict_var) 
  
# Updating existing Key's Value 
dict_var[2] = 'Welcome'
print("\nUpdated key value: ") 
print(dict_var) 
  
# Adding Nested Key value to Dictionary 
dict_var[5] = {'Nested' :{'1' : 'Life', '2' : 'Is','3' : ' Beautiful'}} 
print("\nAdding a Nested Key: ") 
print(dict_var) 




#%%
#Accessing elements of the dictionary --start

#creating an dictionary 
dict_var2 = {1 : 'Pavan',2 : 'Padma', 3 :'Vinaya'}

# accessing a element using key 
print("Acessing a element using key:") 
print(dict_var2[2]) 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(dict_var2[1]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(dict_var2.get(3)) 

#Accessing elements of the dictionary -- End

#%%
#Removing an element from dictionary
# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 
  
# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 
  
# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 
  
# Deleting a Key  
# using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 
  
# Deleting a Key 
# using popitem() 
Dict.popitem() 
print("\nPops first element: ") 
print(Dict) 
  
# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 