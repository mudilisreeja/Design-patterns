#adapter pattern allows objects with incompatible interfaces to work together by wrapping the object with an interface the client expect
class EuropeanSocket:
    def voltage(self):
        return "220V"
class AmericanSocket:
    def voltage(self):
        return "110V"
class SocketAdapter:
    def __init__(self,socket):
        self.socket=socket
        return self.socket.voltage()

european_socket=EuropeanSocket()
adapter=SocketAdapter(european_socket)
print(f"Adapter voltage:{adapter.voltage()}")
