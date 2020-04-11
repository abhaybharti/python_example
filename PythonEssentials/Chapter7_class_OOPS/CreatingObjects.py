class Vehicle:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, model, color):
        self.model = model
        self.color = color


# instantiate the Parrot class
blu = Vehicle("Blu", 10)
woo = Vehicle("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.model, blu.color))
print("{} is {} years old".format(woo.model, woo.color))
