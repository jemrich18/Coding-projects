"""
Jeremiah Emrich
07/02/2025
Show a screenshot of code different that your classmates showing the debugging process.
Version 1
"""
# Import random generator
import random 

# Define main function 
def main():
    emojis = {'r':'🪨', 'p':'📃', 's':'✂️'}
    choices = ('r', 'p', 's')
   # Create a while loop to continue to rerun program until users chooses to exit 
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice not in choices: # Control statement. Tell user input is not valid if r, p, or s is not input. 
            print('Invalid choice!')
            continue # Continue the loop to retart the loop if invalid selection is input 

        
        computer_choice = random.choice(choices)

        
        
        print(f'You chose {emojis[user_choice]}') # Display the users choice back to them 
        print(f'Computer chose {emojis[computer_choice]}') # Display the computers choice back to the user

        if user_choice == computer_choice: # Condition statement indicating both user and computer chose the same object 
            print('Tie!') # Display tie back to the user
        elif (
            (user_choice == 'r' and computer_choice == 's') or # Multi line control statement 
            (user_choice == 's' and computer_choice == 'p') or 
            (user_choice == 'p' and computer_choice == 'r')):
            print("You win!!")
        else: # Condition statement. If the above conditions are not me the user will lose. 
            print('You lose. Sorry') # Display message back to user they lost

        should_continue = input('Continue? (y/n): ').lower() # Get user input on continuing the game or not 
        if should_continue =='n':
            print('Thanks for playing! Goodbye.')
            break # Break the while loop and end the game 


if __name__=='__main__': # Main function call
    main()     