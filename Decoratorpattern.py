#Decorator pattern allows behaviour to be added to individual objects dynamically
class Component:
    def operation(self):
        pass
class ConcreteComponent:
    def operation(self):
        return "concrete component"
class Decorator(Component):
    def __init__(self,component):
        self.component=component
    def operation(self):
        return f"Decorator({self.component.operation()})"

component=ConcreteComponent()
decorator=Decorator(component)
print(decorator.operation())

