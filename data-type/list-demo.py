# %%
# Creating a list
lst_var = [] # Empty list

lst_var = [1,2,3,4,5,5,6,7,8,9,9]
print('List with duplicate elements ', lst_var)

# %%
# Python program to demonstrate  
# accessing of element from list 
  
# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 
  
# accessing a element from the  
# list using index number 
print("Accessing a element from the list") 
print(List[0])  
print(List[2]) 
  
# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List = [['Geeks', 'For'] , ['Geeks']] 
  
# accessing a element from the  
# Multi-Dimensional List using 
# index number 
print("Acessing a element from a Multi-Dimensional list") 
print(List[0][1]) 
print(List[1][0]) 

# %%
# Python program to demonstrate  
# Removal of elements in a List 
  
# Creating a List 
List = ['G','E','E','K','S','F', 
        'O','R','G','E','E','K','S'] 
print("Intial List: ") 
print(List) 
  
# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 
  
# Print elements from a  
# pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(Sliced_List) 
  
# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 

# %%
# Creating a List 
List = ['G','E','E','K','S','F', 
        'O','R','G','E','E','K','S'] 
print("Initial List: ") 
print(List) 
  
# Print elements from beginning 
# to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 
  
# Print elements of a range 
# using negative index List slicing 
Sliced_List = List[-6:-1] 
print("\nElements sliced from index -6 to -1") 
print(Sliced_List) 
  
# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) 


# %%
List = [1,2,3,4,5] 

# Removing element from the 
# Set using the pop() method 
List.pop() 
print("\nList after popping an element: ") 
print(List) 

# Removing element at a 
# specific location from the 
# Set using the pop() method 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 


# %%
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 

# accessing a element using 
# negative indexing 
print("Acessing element using negative indexing") 

# print the last element of list 
print(List[-1]) 

# print the third last element of list 
print(List[-3]) 


# %%
# Python program to demonstrate  
# Addition of elements in a List 
   
# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 
  
# Addition of Element at  
# specific Position 
# (using Insert Method) 
List.insert(3, 12) 
List.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 

# %%
