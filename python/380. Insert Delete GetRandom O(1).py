# i spent a day on it to implement a random function in o(1) time complexity but 
# I gave up and looked at the solution and I found that its permitted to use random library (as all used)


import random
class RandomizedSet:
    def __init__(self):
        self.data = dict()
        # self.random = dict()

    def insert(self, val: int) -> bool:
        if self.data.get(val):
            return False
        else:
            self.data[val] = True
            # self.random[val] = True
            return True

    def remove(self, val: int) -> bool:
        if self.data.get(val):
            self.data.pop(val)
            # self.random.pop(val,False)
            return True
        else:
            return False

    def getRandom(self) -> int:
        # if self.random=={}:
        #     self.random = self.data.copy()
        # item = list(self.random.keys()).pop()
        # self.random.pop(item)
        item = random.choice(list(self.data.keys()))
        return item



# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(0)
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()