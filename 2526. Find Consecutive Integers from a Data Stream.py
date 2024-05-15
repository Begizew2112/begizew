class DataStream:

    def __init__(self, value: int, k: int):
        self.value = []
        self.k = k
        
    def consec(self, num: int) -> bool:
        self.value.append(num)
        
        if len(self.value) == self.k: 
            return True
        
        return False



        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)