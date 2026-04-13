# Scenario: A base class's method is using another method from the base class
# Now if that second method is overriden in the child class
# Now if the child class requires to run the first method (method using another method from its own class)
# The base class will use the method execution which is overriden in its child class for the child object instance
# this will happen if the child class is trying to access the a method from the base class which is using another method 
# from its own class being overriden in the child class.
# to prevent such accidents, we can use name mangling by storing the methods in a mangled variable name

class Base:
    # a function using another function inside itself.
    def execute(self):
        print("Base.execute() running")
        self.__helper()
    # a function being used in another function in it's own class.
    # this same method is overriden in the child class.
    def helper(self):
        print("Base.helper() is running")

    # store the function in a variable which requires name mangling to be updated.
    __helper = helper

class Child(Base):
    def helper(self):
        print("Child.helper() is running")


base = Base()
base.execute() 
## Output: 
# "Base.execute() running"
# "Base.helper() is running"

child = Child()
child.helper()
## Output: 
# "Child.helper() is running"

child.execute()     # this method has no implementation of itself in child class hence calls the implementation from the parent class.
## Output: if __helper is not used.
# "Base.execute() running"
# "Child.helper() is running"       <--------- this is where the break happens as there may be some crucial code being implemented in Base.helper()
#                                              being used by Base.execute() which now has implementation of Child.helper being used
#                                              as self points to the current object instance and execute is using self.helper() to make the call.


base.execute()
# remains the same for the base class object instance.
## Output: 
# "Base.execute() running"
# "Base.helper() is running"