#it is used to encapsulate a request as an object
class Command:
    def execute(self):
        pass
class Light:
    def on(self):
        print("Light is On")
    def off(self):
        print("Light is off")
class Fan:
    def on(self):
        print("fan is On")
    def off(self):
        print("fan is off")
class LightOn(Command):
    def __init__(self,light:Light):
        self.light=light
    def execute(self):
        self.light.on()
class LightOff(Command):
    def __init__(self,light:Light):
        self.light=light
    def execute(self):
        self.light.off()
class FanOn(Command) :
    def __init__(self,fan:Fan):
        self.fan=Fan
    def execute(self):
        self.fan.on(self)
class FanOff(Command):
    def __init__(self,fan:Fan):
        self.fan=Fan
    def execute(self):
        self.fan.off(self)
class RemoteControl:
     def __init__(self):
        self.commands={}
     def set_command(self,button,command:Command):
         self.commands[button]=command
     def press_button(self,button):
         if button in self.commands:
             self.commands[button].execute()
         else:
             print("No command is assaigned to this button")

light=Light()
fan=Fan()
#creating commands
light_on=LightOn(light)
light_off=LightOff(light)
fan_on=FanOn(fan)
fan_off=FanOff(fan)
#setting remote control
remote=RemoteControl()
remote.set_command("A",light_on)
remote.set_command("B",light_off)
remote.set_command("C",fan_on)
remote.set_command("D",fan_off)
#using remote
remote.press_button("A")
remote.press_button("C")
remote.press_button("B")
remote.press_button("D")
