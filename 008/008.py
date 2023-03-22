import random
import sqlite3
import datetime

#forbind
conn = sqlite3.connect('guessing_game.db')
c = conn.cursor()

start_time = datetime.datetime.now()


min_num = 1
max_num = 100


number = random.randint(min_num, max_num)


points = 100


print("Velkommen til gættespillet! Du starter med 100 point.")
print("Jeg tænker på et tal mellem", min_num, "og", max_num, ".")

# Loop until the user guesses the correct number
while True:
    # Get the user's guess
    guess = input("Hvad er dit gæt? ")
    
    # Log the guess in the database
    c.execute("INSERT INTO game_data (start_time, end_time, points) VALUES (?, ?, ?)", 
              (start_time, datetime.datetime.now(), points))
    conn.commit()
    
    # Convert the user's guess to an integer
    try:
        guess = int(guess)
    except ValueError:
        print("Indtast et gyldigttal.")
        continue
    
    # Check if the guess is within the range
    if guess < min_num or guess > max_num:
        print("Indtast et tal mellem", min_num, "og", max_num, ".")
        continue
    
    # Decrement the points for each guess
    points -= 1
    
    # Check if the guess is correct
    if guess == number:
        print("Tillykke! Du gættede tallet på", 100 - points, "forsøg.")
        break
    elif guess < number:
        print("Dit gæt var for lavt. Du har", points, "points tilbage.")
    else:
        print("Dit gæt var for højt. Du har", points, "points tilbage.")

# Update the end time and points in the database
c.execute("UPDATE game_data SET end_time=?, points=? WHERE id=?", 
          (datetime.datetime.now(), points, c.lastrowid))
conn.commit()

# Close the database connection
conn.close()
