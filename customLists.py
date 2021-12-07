class customList:
    def __init__(self, inputList, startsFrom=0):
        self.startsFrom = startsFrom
        self.outputList = inputList
        for i in range(startsFrom):
            self.outputList.insert(i, None)
    def toList(self):
        return self.outputList
    def __getitem__(self, index):
        if index >= self.startsFrom:
            return self.outputList[index]
        else:
            raise Exception("customList index out of range")
    def __setitem__(self, index, value):
        if index >= self.startsFrom:
            self.outputList[index] = value
        else:
            raise Exception("customList index out of range")
    def __iter__(self):
        return iter(self.elements())
    def elements(self):
        return self.outputList[self.startsFrom:len(self.outputList)]
    def insert(self, index, element):
        self.outputList.insert(index, element)
    def pop(self, index):
        self.outputList.pop(index)
    def append(self, element):
        self.outputList.append(element)
    def __len__(self):
        return len(self.elements())
