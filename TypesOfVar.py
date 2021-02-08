#there are two types of variables and 3 types of methods
#instance Variables and class Variables or static variables
#three types of methods 1.Instance methods,2.Class Methods,3.Static Methods

#Instance Variables

class Parent:
    c=100   #This is Class Variable or Static Variable
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("These are Instance Variables:",self.a,self.b)
    @classmethod
    def ClassMethod(cls):
        print("Class Method",cls.c)
    @staticmethod
    def StaticMethod():
         print("WElcome to static Methods")

p=Parent(20,30)
p.show()
print("This is class variable and accessing through object of that class",p.c)

print("This is class variable or instance variable and can be accessed with class name",Parent.c)

#methods

# the show method above is a instance method as we are passing the variables instantly

Parent.ClassMethod()   # we can access the class method with class name no need to create the object,we need to use
                         #@classmethod decorator

#static method
Parent.StaticMethod()  #static Method does not take self,cls as variable inside the braces.. they can be accessed with
                        #class name no need to create object just like class methods.
