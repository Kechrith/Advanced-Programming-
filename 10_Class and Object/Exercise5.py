"""
Your  program  should  work  with  Candidates.csv  file  to  store  and  retrieve  candidate  information. 
When the program starts, check if the Candidates.csv file exists or not. If the file does not exist, create 
it  with  the  following  headers:  ID,  Name,  Gender,  Favorite_Color,  Favorite_Fruit,  Hobby.
"""

import csv
import os

# Person Class
class Person:
    def __init__(self, id, name, gender, favorite_color, favorite_fruit, hobby):
        self.id = id
        self.name = name
        self.gender = gender
        self.favorite_color = favorite_color
        self.favorite_fruit = favorite_fruit
        self.hobby = hobby

# Matchmaker class
class Matchmaker:
    def __init__(self):
        self.candidates = []

    # Load condidate from csv file
    def load_from_file(self, filename):
        self.candidates = []
        if os.path.exists(filename):
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    person = Person(
                        row['ID'],
                        row['Name'],
                        row['Gender'],
                        row['Favorite_Color'],
                        row['Favorite_Fruit'],
                        row['Hobby']
                    )
                    self.candidates.append(person)

    # Add new candidate to csv file and list
    def add_candidate(self, person, filename):
        file_exists = os.path.exists(filename)

        with open(filename, mode='a', newline='') as file:
            fieldnames = ['ID', 'Name', 'Gender', 'Favorite_Color', 'Favorite_Fruit', 'Hobby']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                'ID': person.id,
                'Name': person.name,
                'Gender': person.gender,
                'Favorite_Color': person.favorite_color,
                'Favorite_Fruit': person.favorite_fruit,
                'Hobby': person.hobby
            })

        self.candidates.append(person)

    # Display all candidates
    def display_all(self):
        if not self.candidates:
            print("No candidates found.")
            return

        for p in self.candidates:
            print(f"{p.id}, {p.name}, {p.gender}, {p.favorite_color}, {p.favorite_fruit}, {p.hobby}")

    # Find best match based on preferences
    def find_match(self, person):
        best_score = -1
        best_matches = []

        for candidate in self.candidates:
            score = 0

            if person.favorite_color == candidate.favorite_color:
                score += 4
            if person.favorite_fruit == candidate.favorite_fruit:
                score += 3
            if person.hobby == candidate.hobby:
                score += 3

            if score > best_score:
                best_score = score
                best_matches = [candidate]
            elif score == best_score:
                best_matches.append(candidate)

        if best_score <= 0:
            print("No good match found.")
        else:
            print(f"Best Match Score: {best_score}/10")
            for match in best_matches:
                print(f"- {match.name} ({match.gender})")

# Function to display options and let user choose
def choose_option(options, message):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input(message))
    return options[choice - 1]

# main program
def main():
    filename = "Candidates.csv"
    colors = ["Red", "Green", "Blue", "Yellow", "Black", "White", "Pink", "Purple", "Orange", "Brown"]
    fruits = ["Apple", "Banana", "Mango", "Orange", "Grape", "Pineapple", "Watermelon", "Cherry", "Peach", "Strawberry"]
    hobbies = ["Reading", "Gaming", "Traveling", "Cooking", "Sports", "Music", "Dancing", "Drawing", "Fishing", "Shopping"]
    matchmaker = Matchmaker()
    matchmaker.load_from_file(filename)
    while True:
        print("Cupid’s Matchmaking System ")
        print("1. Add a new candidate")
        print("2. Find a match")
        print("3. Display all candidates")
        print("4. Exit")
        choice = input("Choose an option: ")

        # Option 1
        if choice == "1":
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            gender = input("Enter Gender: ")
            favorite_color = choose_option(colors, "Select your favorite color: ")
            favorite_fruit = choose_option(fruits, "Select your favorite fruit: ")
            hobby = choose_option(hobbies, "Select your hobby: ")
            person = Person(id, name, gender, favorite_color, favorite_fruit, hobby)
            matchmaker.add_candidate(person, filename)
            print("Candidate added successfully!")

        # Option 2
        elif choice == "2":
            name = input("Enter your Name: ")
            gender = input("Enter your Gender: ")
            favorite_color = choose_option(colors, "Select your favorite color: ")
            favorite_fruit = choose_option(fruits, "Select your favorite fruit: ")
            hobby = choose_option(hobbies, "Select your hobby: ")
            person = Person("0", name, gender, favorite_color, favorite_fruit, hobby)
            matchmaker.find_match(person)

        # Option 3
        elif choice == "3":
            matchmaker.display_all()

        # Option 4
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
# Run the program
main()