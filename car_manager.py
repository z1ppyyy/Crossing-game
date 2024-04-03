from turtle import Turtle
from random import choice,randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_speed = 0.1

    def create_car(self):
            random_chance = randint(1,6)
            if random_chance == 1:
                new_car = Turtle("square")
                new_car.color(choice(COLORS))
                new_car.penup()
                new_car.shapesize(1,2)
                random_y = randint(-250,250)
                new_car.goto(x=300,y=random_y)
                self.cars.append(new_car)

    def move_cars(self):
         for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
            
    def bounce(self):
        self.move_speed *= 0.7
         

         
        


    
        
        

    
