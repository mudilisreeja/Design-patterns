#creating objects that involves multiple steps
class Burger:
    def __init__(self):
        self.ingrediants=[]
    def add_ingrediant(self,ingrediant):
        self.ingrediants.append(ingrediant)
    def __str__(self):
        return "Burger with "+",".join(self.ingrediants)
class BurgerBuilder:
    def __init__(self):
        self.burger=Burger()
    def add_bun(self):
        self.burger.add_ingrediant("bun")
        return self
    def add_patty(self):
        self.burger.add_ingrediant("patty")
        return self
    def add_lettuce(self):
        self.burger.add_ingrediant("lettuce")
        return self
    def build(self):
        return self.burger
builder=BurgerBuilder()
burger=builder.add_patty().add_bun().add_lettuce().build()
print(burger)

