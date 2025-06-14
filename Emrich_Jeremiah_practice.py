import turtle

WIDTH, HEIGHT = 500, 500

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try again!')
            continue

        if 2 <= racers <=10:
            return racers
        else: 
            print('Number not in range 2 - 10. Try agian!')

def init_turtle():
    Screen = turtle.Screen()
    Screen.setup(WIDTH, HEIGHT)
    Screen.title('Turtle Racing!')


racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.speed(1)
racer.penup()
racer.shape('turtle')
racer.color('blue')
racer.forward(100)
racer.left(90)
racer.penup()
racer.forward(100)
racer.right(90)
racer.backward(100)

racer2 = turtle.Turtle()
racer2.speed(5)
racer2.penup()
racer2.shape('turtle')
racer2.color('red')
racer2.forward(150)
racer2.left(90)
racer2.penup()
racer2.forward(150)
racer2.right(90)
racer2.backward(100)

