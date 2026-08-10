import random

print()
print('''[======================]
  NUMBER GUESSING GAME
[======================] ''')

print ("\nDo you want to play? yes/no")
player_1 = input("> ").strip().lower()
print()


while player_1 not in ["yes", "no"]:
    print("Invalid Input only yes/no")
    player_1 = input("> ").strip().lower()

if player_1 == "no":
  print("Okay, maybe next time!")
  print()

elif player_1 == "yes":
    
    select_range = int(input("Select the number to range from: (ex: 10,5,22)\n> "))
    secret_number = random.randint(1, select_range)
    tries = int(input("Select the number of tries: (ex: 3,5,13)\n> "))
    
    while tries != 0:
      guess = int(input(f"Enter your guess (1 to {select_range}): "))
      
      if guess == secret_number:
         print(f"🎉 Congratulations! You guessed the secret number: {secret_number}!")
         break
       
      else:
        tries -= 1
        if guess > secret_number:
          print(f"Wrong guess! Try again. You have {tries} attempt left hint: Lower⬇️")
        else:
          print(f"Wrong guess! Try again. You have {tries} attempt left hint: Higher⬆️")
      
      if tries == 0:       
              print(f"""
      +------------------------------+
      |        G A M E  O V E R       |
      |    Better luck next time!     |
      |       Secret number:{secret_number}         |
      +------------------------------+
      """) 