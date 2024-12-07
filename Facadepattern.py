#Facade pattern provides a simplified interface to a larger body of code
class SubsystemA:
    def operation(self):
        return "SubsystemA:Ready!"
class SubsystemB:
    def operation(self):
        return "SubsystemB:Go!"
class Facade:
    def __init__(self,):
        self.subsystem_a=SubsystemA()
        self.subsystem_b=SubsystemB()
    def operation(self):
        result=[]
        result.append(self.subsystem_a.operation())
        result.append(self.subsystem_b.operation())
        return "\n".join(result)

facade=Facade()
print(facade.operation())
