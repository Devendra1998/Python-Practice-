class person:
    def __init__(self,name,age,):
        self.name=name
        self.age=age


    def  myfunc(self):
        print("hello my age is " , self.age)

p1 = person("Deva", 22)
p1.myfunc()
del p1.age
