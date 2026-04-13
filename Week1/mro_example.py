class Base:
    def process(self):
        print("Base here.")

class Left(Base):
    def process(self):
        print("\"Left\" here.")
        # without MRO it would have called this right away.
        super().process()
       
class Right(Base):
    def process(self):
        print("\"Right\" here.")
        # without MRO it would have called this right away.
        super().process()

class Child1(Left, Right):
    def process(self):
        print("Child here.")
        # without MRO it would have Base.process 2 times. Once for Left.process() and once for Right.process()
        super().process()

class Child2(Right, Left):
    def process(self):
        print("Child here.")
        # without MRO it would have Base.process 2 times. Once for Left.process() and once for Right.process()
        super().process()

child1 = Child1()
child1.process()
print("-" * 15)
child2 = Child2()
child2.process()
