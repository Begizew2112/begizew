
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if len(words)< 2:
            return []
        char_freqs = {}
        for char in words[0]:
            char_freqs[char] = char_freqs.get(char, 0) + 1

        for word in words[1:]:
            word_freqs = {}
            for char in word:
                word_freqs[char] = word_freqs.get(char, 0) + 1

            for char in char_freqs:
                if char in word_freqs:
                    char_freqs[char] = min(char_freqs[char], word_freqs[char])
                else:
                    char_freqs[char] = 0
        result = []
        for char, freq in char_freqs.items():
            result.extend([char] * freq)

        return result


