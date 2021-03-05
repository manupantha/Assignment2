class Vehicle:
    color = "black"
    doors = '4'

    def change_color(self, color):
        self.color = color


class Car(Vehicle):
    def change_color(self, color):
        print("color of car is changed")
        super().change_color(color)


class Bike(Vehicle):
    doors = 0


c = Car()
print(c.color)
print(c.doors)
c.change_color('blue')
print(c.color)

