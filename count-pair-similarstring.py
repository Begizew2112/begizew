class Solution:
    def similarPairs(self, words: list[str]) -> int:
        if len(words) < 2:
            return 0
        
        words = [''.join(set(word)) for word in words]
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j] == words[i]:
                    count += 1
        return count
