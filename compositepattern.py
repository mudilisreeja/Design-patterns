#composite pattern allows let clients treat individual objects and composite objects uniformly
class Component:
    def operation(self):
        pass
class Leaf(Component):
    def operation(self):
        print("Leaf operation")
class Composite(Component):
    def __init__(self):
        self.children=[]
    def add(self,Component):
        self.children.append(Component)
    def operation(self):
        print("composite operation")
        for child in self.children:
            child.operation()
leaf1=Leaf()
leaf2=Leaf()
composite=Composite()
composite.add(leaf1)
composite.add(leaf2)
composite.operation()

