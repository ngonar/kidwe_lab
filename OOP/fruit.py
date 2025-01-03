class Fruit:
    species = "fruit"

    def __init__(self, name, color):
        self.name = name
        self.color = color


apple = Fruit("Apple", "red")
print(apple.name)
print(apple.color)

pear = Fruit(name="Pear", color="blue")
print(pear.name)
print(pear.color)