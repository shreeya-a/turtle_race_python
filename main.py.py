import random
import tkinter as tk
from tkinter import messagebox
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? {colors} Enter a color: ")
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # turtle_red.goto(x=-230, y=-60 + turtle_index * 25)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


# funtion to show result pop-up
def show_result(winning_color):
    root = tk.Tk()
    root.withdraw()
    if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
        messagebox.showinfo("Turtle says:", f"You've won! The {winning_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
        messagebox.showinfo("Turtle says:", f"You've lost! The {winning_color} turtle is the winner!")
    root.destroy()


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            show_result(winning_color)
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# screen.exitonclick()
