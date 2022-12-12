class TV:
    def __init__(self):
        self.is_on=False

    def turn_on(self):
        self.is_on=True

    def turn_off(self):
        self.is_on=False

    def show_status(self):
        if self.is_on:
            print("Tv is on")
        else:
            print("Tv is off")
            
        # print("Tv is on") if self.is_on else print("Tv is off")

tv1=TV()
tv1.turn_on()
tv1.show_status()
        
