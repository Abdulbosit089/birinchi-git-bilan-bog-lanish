class Time:
    hour=int(input("Soat:"))
    min=int(input("Minut:"))
    sec=int(input("Sekund:"))
    def chiqarish(self):
        if self.hour>=24:
            self.hour-=24
        if self.min>=60:
            self.hour+=1
            self.min-=60
        if self.sec>=60:
            self.min+=1
            self.sec-=60
        print(f"{self.hour}:{self.min}:{self.sec}")
class Hour(Time):
    def oshirish(self):
        self.hour+=5
               
class Minut(Time):
    def oshirish(self):
        self.min+=5
class Sec(Time):
    def oshirish(self):
        self.sec+=5
a=Time
b=int(input("1-Soatni oshirish,2-Minutni oshirish,3-Sekundni oshirish:"))
if b==1:
    b=Hour
    b.oshirish()
    b.chiqarish()
elif b==2:
    b=Minut
    b.oshirish
    b.chiqarish()
elif b==3:
    b=Sec
    b.oshirish()
    b.chiqarish
#ddddd
