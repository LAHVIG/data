import json
import os

# Directory containing JSON files

# List to store all "navn" values found in JSON files
navn_values = []
filenames = ["name.json", "weather.json"]


def find_value(key,files):
    for filename in files:
        if filename.endswith(".json"):
            # Read JSON file
            with open(os.path.join(os.getcwd(), filename), "r") as json_file:
                data = json.load(json_file)
                
            for i in data:
                if key in i:
                    navn_values.append(i[key])

# Print all "navn" values found in JSON files
search = input("search for: ")
find_value(search, filenames)
print(navn_values)