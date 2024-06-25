class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {}
        for i , char in enumerate(s):
            last_index[char] = i
        print(last_index) #{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        #s = "ababcbacadefegdehijhklij"
        result =[]
        size = 0 
        end = 0
        for i , char in enumerate (s):
            size +=1
            end = max( end, last_index[char])
            if i == end :
                result.append(size)
                size = 0
        return result