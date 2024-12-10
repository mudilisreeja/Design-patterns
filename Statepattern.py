#state design pattern allows an object to change its behaviour when its internal state changes
from abc import ABC,abstractmethod
class TrafficLightState(ABC):
    def handle(self,context):
        pass
class RedState(TrafficLightState):
    def handle(self,context):
        print("Stop!.. red light is on")
        context.set_state(GreenState())
class GreenState(TrafficLightState):
    def handle(self,context):
        print("Go! The light is green")
        context.set_state(YellowState())
class YellowState(TrafficLightState):
    def handle(self,context):
        print("Caution! the yellow light is on")
        context.set_state(RedState())
class TrafficLight:
    def __init__(self,state):
        self._state=state
    def set_state(self,state):
        self._state=state
    def request(self,state):
        self._state.handle(self)
#client mode
from abc import ABC, abstractmethod

class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class RedState(TrafficLightState):
    def handle(self, context):
        print("Stop!.. red light is on")
        context.set_state(GreenState())

class GreenState(TrafficLightState):
    def handle(self, context):
        print("Go! The light is green")
        context.set_state(YellowState())

class YellowState(TrafficLightState):
    def handle(self, context):
        print("Caution! The yellow light is on")
        context.set_state(RedState())

class TrafficLight:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle(self)

# Client code
if __name__ == "__main__":
    traffic_light = TrafficLight(RedState())
    for _ in range(6):
        traffic_light.request()



