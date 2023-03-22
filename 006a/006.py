#SQL fra Python​
#
#    Lav Python kode som generer "temperatur" i 50 forskelige byer. Der skal genereres ca. 10000 målinger.​
#
#    Alt dat skal opbevares i en database.
#
#    Der skal skrives ud alle værdier for Aarhus.
#
#    Der skal skrives ud alle de byer og deres temperatur for de 10 koldeste og varmeste værdier.
#
#    Der skal skrives ud allersidste måling.
#
#    Alle udskrivelser skal ske live


import csv

# specify the path to the csv file
csv_file_path = 'city_temperature.csv'

# create empty lists to hold the relevant data
copenhagen_temps = []
all_temps = []

# read in the csv file
with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # check if the city is Copenhagen
        if row['City'] == 'Copenhagen':
            copenhagen_temps.append(float(row['AvgTemperature']))
        
        # add all temperatures to the all_temps list
        all_temps.append(float(row['AvgTemperature']))

# sort the all_temps list in ascending order
all_temps.sort()

# print out the 10 coldest and 10 hottest temperatures
print(f'The 10 coldest temperatures are: {all_temps[:10]}')
print(f'The 10 hottest temperatures are: {all_temps[-10:]}')


# print out all temperatures from Copenhagen
print(f'All temperatures from Copenhagen are: {copenhagen_temps}')
