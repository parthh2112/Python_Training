
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, t1, t2):
        total_minutes = (t1.hours + t2.hours)*60 + t1.minutes + t2.minutes
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60

    def displayTime(self):
        print(f"Time: {self.hours} hr {self.minutes} min")
    
    def displayMintute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")
       

t1 = Time(2, 50)
t2 = Time(1, 20)

t3 = Time(0,0)
t3.addTime(t1, t2)

t3.displayTime()
t3.displayMintute()