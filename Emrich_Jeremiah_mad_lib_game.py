def welcome():
    print("Welcome to my mad libs program. Hope you enjoy this fun and exciting word game.") # Welcome user to my game.


# Get users input: users name, 2 verbs, 2 nouns, 2 adjectives and 2 integers.
def main():
    name = input ("Please enter your name: ").title() # Get users name. Format to title capitalizing first and last name.
    verb_1 = input ("Please enter a verb: ").lower() # Get users verb. lower case format
    verb_2 = input ("Please enter another verb: ").lower()
    noun_1 = input ("Please enter a noun: ")
    noun_2 = input("Please enter another noun: ")
    adj_1 = input ("Please enter a adjective: ").lower()
    adj_2 = input("Please enter another adjective: ").lower()
    num_1 = int(input("Please enter a number (whole numbers only!): "))
    num_2 = int(input("Please enter another number (whole numbers only!): "))

# Present to the user the name of the mad lib program
    print("Princess in perile mad lib.")
#Using an f string enter user input into the mad lib story.
    print(f"""Once upon a time there was a knight named {name}. The knight was directed by the king to {verb_1} the 
{noun_2} and rescue the princess. The knight was given {num_1} swords and {num_2} knights to help.
Led by {name} the knights {verb_2} into the cold {adj_2} filled night to persue the {noun_2}.
After two days of riding they reached the abandoned castle where the {adj_1} princess was
held captive. 
The knights slayed the {noun_1} and returned the princess back to the king. They were local heros. 
""")
# Ask user if they want to continue playing the game
    while True: #
        keep_playing = input("Do you want to keep playing? (enter to continue / no will exit): ").lower()
        if keep_playing == "no": #Condition statement. Once user enters "no" they will exit the game.
            print("Thank you for playing. Goodbye!")
            break # Once "no" is inputted the while loop will be broken.
        else: # as long as "no" is not entered the game will continue to play and prompt the user to enter their name.
            main()


# Call the functions
if __name__ == '__main__':
    welcome()
    main()