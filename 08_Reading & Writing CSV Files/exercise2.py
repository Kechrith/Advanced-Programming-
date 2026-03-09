# Exercise 2: Read Products.csv and save products with price > 50 into Expensive_products.csv

import csv  # Import CSV module

# Open Products.csv to read data
with open("Products.csv", "r", newline="") as infile:
    
    # Create reader object (read rows as dictionary)
    reader = csv.DictReader(infile)
    
    # Open new file to save filtered products
    with open("Expensive_products.csv", "w", newline="") as outfile:
        
        # Create writer object with same column names
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write header row to new file
        writer.writeheader()
        
        # Loop through each row in Products.csv
        for row in reader:
            
            # Check if Price is greater than 50
            if float(row["Price"]) > 50:
                
                # Write the row to new file
                writer.writerow(row)

print("Exercise 2 completed: Expensive_products.csv created successfully.")