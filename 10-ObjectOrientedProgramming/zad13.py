class TV:
    volume=0
    def show_status(self):
        print(f"Current volume: {self.volume}")
    def increase(self):
        if self.volume<10:
            self.volume+=1
    def decrease(self):
        if self.volume>0:
            self.volume-=1

tv=TV()
tv.show_status()
tv.increase()
tv.show_status()
tv.decrease()
tv.show_status()
