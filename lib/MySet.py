class MySet:

    def __init__(self, enumerable=[]) -> None:
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def __str__(self) -> str:
        ls = []
        for key in self.dictionary.keys():
            ls.append(str(key))
        return f'MySet: {{{",".join(ls)}}}'


    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value]=True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self
    
    


st = MySet([1,2,3,3,3,4])

st.add(5)
print(st.add(6))
print(st.delete(7))
print(st.size())
print(st.clear())