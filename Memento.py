#it provides storing the internal state of object without violating the encapsulation.used in undo/redo operations.
class Memento:
    def  __init__(self,state):
        self.state=state
    def getstate(self):
        return self.state
class TextEditor():
    def __init__(self):
        self.state=""
    def write(self,text):
        self.state += text
    def save(self):
        return Memento(self.state)
    def restore(self,memento):
        if memento:
           self.state=memento.getstate()
        else:
            print("No state to restore")
    def show_content(self):
        print(f"current content:{self.state}")
class History:
    def __init__(self):
        self._mementos=[]
    def push(self,memento):
        self._mementos.append(memento)
    def pop(self):
        if self._mementos:
            return self._mementos.pop()
        return None
editor=TextEditor()
history=History()
editor.write("hello")
editor.show_content()
editor.write("world!")
editor.show_content()
history.push(editor.save())
editor.write("Lets undo")
editor.show_content()
editor.restore(history.pop())
editor.show_content()
editor.restore(history.pop())
editor.show_content()



