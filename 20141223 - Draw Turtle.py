import turtle

def draw_square(brad):

    for i in range(4):
        brad.forward(100) #amount to go forward
        brad.right(90)  #want to change the direction by 90 degrees

def draw_art():
    brad = turtle.Turtle()  #customizing the arrow into a turtle
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    #can also customize its speed. speed can only go from 1 to 10

    for i in range (36):
        draw_weirdshape(brad)
        brad.right(10)
        
def draw_weirdshape(pointer):
    pointer.forward(100)
    pointer.left(90)
    pointer.forward(45)
    pointer.right(120)
    pointer.forward(100)
    pointer.right(120)
    pointer.forward(100)
    pointer.right(120)
    pointer.forward(45)
    pointer.left(90)
    pointer.forward(100)
    
window = turtle.Screen()    #this creates a screen
window.bgcolor("red")   #setting the background of screen to red
    
draw_art()

window.exitonclick()    #here we make sure that the screen is closing
