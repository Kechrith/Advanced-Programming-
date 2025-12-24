'''A program asks to merge two dictionaries.
    If a key appears in both dictionaries, add their values.
    If a key appears in only one dictionary, keep its value.'''

# 1&2 dictionary 
dict1= {'a':10,'b':20,'c':30}
dict2= {'b':15,'c':25,'d':35}

# copy dict1 into results 
results = dict1.copy()

# loop through each key in dict2
for k in dict2:
    # if key already exists in results
    if k in results:
        # add the value from dict2 to existing value
        results[k] += dict2[k]
    # if key does not exist, add it to results
    else:
        results[k] = dict2[k]
#display the results
print(results)