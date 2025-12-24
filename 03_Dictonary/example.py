# Display the following table

table_infor = {
    "ID": [1, 2, 3],
    "Name": ["Chan Dara", "Keo Sela", "Sovanratanak"],
    "Age": [20, 19, 21]
}

# Print table
print('-' * 50)
for key in table_infor.keys():
    print(key.ljust(15), end="")
print()
print('-' * 50)

for i in range(len(table_infor["ID"])):
    for key in table_infor.keys():
        print(str(table_infor[key][i]).ljust(15), end="")
    print()
print('-' * 50)