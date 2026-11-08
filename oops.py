# introduction to oops
# object oriented programming


# attributes and behaviour


# class car:
#     def start():        #methods
#         print("car satrts")
#         def stops():
#             print("car has stopped")


# car1=car
# car2=car
# car3=car
# print(car1)
# car1.start()


# constructor


# class car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def start(self):
#         print("car starts")

#     def stops(self):
#         print("car has stopped")


# car1 = car("swift", "brown")
# print(car1.color, car1.name)

# car2 = car("honda city", "Red")
# print(car2.color, car2.name)


class pen:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def compare(self, other):
        print(self.name)


pen1 = pen("point", 20)
pen2 = pen("lexi", 10)

pen2.compare(pen1)