class singleton:
    _instance=None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance=super().__new__(cls)
        return cls._instance

s1=singleton()
s2=singleton()
print(s1 is s2)
