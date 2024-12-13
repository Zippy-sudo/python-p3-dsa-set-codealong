class MySet:
    def __init__(self, list = []):
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        if value in self.dictionary == True:
            return self
        else:
            self.dictionary[value] = True
            return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)