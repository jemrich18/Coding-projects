"""
Name: Jeremiah Emrich
Date: 06/11/2025
Assignment: Week 5 discussion - functions
Version 1
"""


# Ask for the users name for the credit application. 
def main(name = input, age = input):
  name = input("Please enter your name: ")
  age = int(input("Please enter your age: "))  
  if age < 18: # control statement. if the user is less than 18 they are not eligible for a credit card. 
    print('You are not old enough for a credit card. ') # if the user is under the age of 18 they are not eligible. 
  else: # control statement. If the user is over the age of 18 they can be signed up for a credit card
    print('You are now signed up.') # everyone over the age of 18 is eligible for the credit card.

   

    
if __name__ =="__main__":
    main(input, input)


    





