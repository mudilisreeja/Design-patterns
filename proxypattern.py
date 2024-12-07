#proxy pattern provides a placeholder for another object to control access to it
class RealSubject:
    def request(self):
        return "Realsubject:Handling request"
class Proxy:
    def __init__(self):
        self.real_subject=RealSubject()
    def request(self):
        print("proxy:checking access")
        return self.real_subject.request()

proxy=Proxy()
print(proxy.request())
