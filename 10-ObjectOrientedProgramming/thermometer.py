import random

class Thermometer:  
    def __init__(self):
        self.turning_on=False
        self.temp=None

    def turn_on(self):
        self.turning_on=True

    def turn_off(self):
        self.turning_on=False

    def measure(self):
        if self.turning_on:
            self.temp=random.randint(340,420)/10
        
    def display(self):
        if self.turning_on and self.temp!=None:
            print(f"Temperature: {self.temp}C", end=" ")
            if self.temp>=37.0:
                print("(Fever)", end="")
                if self.temp>=41.0:
                    print(" CRITICIAL TEMPERATURE!!")