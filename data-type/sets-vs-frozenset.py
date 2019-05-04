# Python program to demonstrate differences 
# between normal and frozen set 

#%%
# Same as {"a", "b","c"} 
normal_set = set(["a", "b","c"]) 

# Adding an element to normal set is fine 
normal_set.add("d") 

print("Normal Set") 
print(normal_set) 

# A frozen set 
frozen_set = frozenset(["e", "f", "g"]) 

print("Frozen Set") 
print(frozen_set) 

# Uncommenting below line would cause error as 
# we are trying to add element to a frozen set 
# frozen_set.add("h") 
