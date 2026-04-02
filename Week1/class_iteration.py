class Name:
    def __init__(self, name):
        self.data = name
        self.length = len(name)
        self.index = 0

    def __iter__(self):
        ### generator usage when you don't need to write a lot of code for __next__
        # for i in range(0, self.length):
        #     yield self.data[i]

        return self
    
    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            value = self.data[self.index]
            self.index += 1
            return value
        
name = Name("Harsh")
for char in name:
    print(char)
        