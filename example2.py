class Vehicle:
    doors = 4

    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def make_it_green(self):
        self.color = "green"

    def get_info(self):
        return f"{self.color} vehicle  has milage {self.milage}"

    def change_doors(self):
        self.doors = 3


v1 = Vehicle("black", 30)
Vehicle1 = Vehicle("red", 25)
Vehicle2 = Vehicle('white', 20)

# print(Vehicle2.milage)
# print(Vehicle2.color)
# print(Vehicle1.get_info())
# Vehicle1.make_it_green()
# print(Vehicle1.color)
# print(Vehicle1.doors)
# Vehicle1.change_doors()
# print(Vehicle1.doors)
print(v1.doors)  # call through object
v1.change_doors()
print(v1.doors)
print(Vehicle1.doors)
