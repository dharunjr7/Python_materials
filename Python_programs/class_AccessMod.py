
class A:
    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
        print(self.__priv)        

obj = A()

print(obj.pub)
print(obj._prot)
print(obj.__priv)
    
    
# public - its accessible gloabally
#protected - starts with '_' and its accessible in other classes as well
#private - starts with '__' and it is accessible only within the class & not outside the class