#observe design pattern where an object maintains list of its dependents and notifies them of any state changes usually by calling one of their methods
#subject interface
class Subject:
    def __init__(self):
        self.observers=[]
    def add_observers(self,observer):
        self.observers.append(observer)
    def remove_observers(self,observer):
        self.observers.remove(observer)
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
#concrete subject
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self.temperature=None
    def set_temperature(self,temperature):
        print(f"Weather station:Temperature updated to{temperature}")
        self.temperature=temperature
        self.notify_observers()
    def get_temperature(self):
        return self.temperature
#observer interface
class Observer:
    def update(self,subject):
        pass
class PhoneDisplay(Observer):
    def update(self,subject):
        if isinstance(subject,WeatherStation):
            print(f"phone display:temperature now is{subject.get_temperature()}")
class WindowDisplay(Observer):
    def update(self,subject):
        if isinstance(subject,WeatherStation):
            print(f"window display:temperature now is {subject.get_temperature()}")

weather=WeatherStation()
phone_display=PhoneDisplay()
window_display=WindowDisplay()
weather.add_observers(phone_display)
weather.add_observers(window_display)
weather.set_temperature(32)
weather.set_temperature(28)
weather.remove_observers(phone_display)
weather.set_temperature(20)
