class MySet:
    def __init__(self,enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    def has(self,value):
            return value in self.dictionary
    
    def __str__(self):
         list= []
         for key,value in self.dictionary.items():
              list.append(str(key))
         return f'Set:{{{",".join(list)}}}'
    
    def add(self,value):
         self.dictionary[value] =True
         return self
    
    def delete(self,value):
         self.dictionary.pop(value, None)
         return self
    
    def size(self):
         return len(self.dictionary)
    
    def clear(self):
         self.dictionary.clear()


