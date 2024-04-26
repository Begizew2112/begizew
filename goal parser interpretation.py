class Solution:
    def interpret(self, command: str) -> str:
        result = []
        for i in range(len(command)):
            if command[i] == 'G':
                result.append( command[i] )
            elif command[i] =='(' or command[i] == 'a':
                continue
            elif command[i] ==')' and command[i-1] == '(':
                result.append('o')
            elif command[i] =='l' and command[i-1] == 'a':
                result.append('al')
        return  ''.join(result)


            