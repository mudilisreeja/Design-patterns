#creates new objects by copying existing ones rather than instantiating new objects
import copy
class prototype:
    def __init__(self,value):
        self.value=value
    def clone(self):
        return copy.deepcopy(self)
original=prototype("original value")
clone=original.clone()
print(clone.value)