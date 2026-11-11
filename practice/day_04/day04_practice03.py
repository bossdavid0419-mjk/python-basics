color = "blue"

for i in range(3):
    user_input = input("Guess my favorite color:")
    if user_input.lower() == color:
        print("You guessed it!")
        break
    else:
        print(f"Sorry, the correct answer is {color}.")
        