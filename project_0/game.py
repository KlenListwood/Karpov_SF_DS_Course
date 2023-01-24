"""Guess the number"""

import numpy as np

number = np.random.randint(1,101) #set the number

#quantity of tries
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("The Number should be less!")

    elif predict_number < number:
        print("The Number should be greater!")

    else:
        print(f"You've guessed the number right! The Number is = {number}, in {count} tries")
        break # the end of the game, quit the cycle
# Со второй попытки