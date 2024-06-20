#394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        stack_count = []
        stack_result = []
        result = ""
        count = 0
        
        for char in s:
            if char.isdigit():
                count = count * 10 + int(char)
            elif char == '[':
                stack_count.append(count)
                stack_result.append(result)
                count = 0
                result = ""
            elif char == ']':
                last_count = stack_count.pop()
                last_result = stack_result.pop()
                result = last_result + last_count * result
            else:
                result += char
        
        return result

        
