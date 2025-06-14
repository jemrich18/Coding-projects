"""
Name: Jeremiah Emrich
Date: 06/11/2025
Assignment: Week 5 discussion - functions
Version 1
"""


# Ask for the users name for the credit application. 
name = input('Please enter your fisrt and last name: ')
 
def credit_app(name):
  if name == "": # let the user know they didnt enter their name and prompt them to enter their name again. 
    print('You did not enter your name. ')  
    print(name)
    
    


def age(age):
  age = int(input('Please enter your age: ')) # request the users age. 
  if age < 18:
    print('You are not old enough for a credit card. ') # if the user is under the age of 18 they are not eligible. 
  else:
    print('You are now signed up.') # everyone over the age of 18 is eligible for the credit card. 

   

    
if __name__ =="__main__":
  credit_app(name)
  age(age)


    





