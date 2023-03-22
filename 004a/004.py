import csv

# specify the file path for the CSV file
csv_file_path = "PTOE.csv"

# open the CSV file and read the contents into a list
with open(csv_file_path, "r") as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)

# prompt the user for a keyword to search for
keyword = input("Enter a keyword to search for: ")

# loop through each row in the data list
for i in range(1, len(data)):
    # loop through each column in this row
    for j in range(len(data[i])):
        # check if the keyword appears in this column (ignoring case)
        if keyword.lower() in data[i][j].lower():
            # if so, print out the entire row
            print(",".join(data[i]))
            # break out of the inner loop to avoid printing the row multiple times
            break

# prompt the user to enter a new row to add to the CSV file
new_row = input("Enter a new row to add to the CSV file: ")

# split the new row into a list of values
new_row_values = new_row.split(",")

# append the new row to the data list
data.append(new_row_values)

# open the CSV file and write the updated data back to it
with open(csv_file_path, "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
