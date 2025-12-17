"""Ask the user to enter the names of three people they want to invite to a party and store them in a list. 
After they have entered all three names, ask them if they want to add another. If they do, allow them 
to add more names until they answer “no”. When  they answer “no”, display how many people they 
have invited to the party."""

# Store their names in the list
name_list = []

# check the duplicate 
name_initial = input("Enter three names of people you want to invite (using comma): ").strip()
for name in name_initial.split(','):
    cleaned_name = name.strip()
    if cleaned_name and cleaned_name not in name_list:
        name_list.append(name)
    
while True:
    add_name = input("Would you want to add other people to join? Yes/NO: ").lower()

    if add_name == 'no':
        break
    elif add_name == 'yes':
        new_name = input ("Enter people you want to invite: ").strip()
        if new_name and new_name not in name_list:
            name_list.append(new_name)
    else:
        print("Please Enter Yes or No!!")
    
# Display The Names
print('=' * 35)
print("The Name that You invited to the party:")
for index, name in enumerate(name_list, 1):
    print(f"{index}.{name.strip()}")

    