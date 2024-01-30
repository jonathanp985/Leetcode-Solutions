class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        prev = []
        for token in tokens:
            if token == '+':
                int1 = prev.pop()
                int2 = prev.pop()
                prev.append(int(int1) +  int(int2))
            elif token == '-':
                int1 = prev.pop()
                int2 = prev.pop()
                prev.append(int(int2) - int(int1))
            elif token == '/':
                int1 = prev.pop()
                int2 = prev.pop()
                prev.append(int(int2) /  int(int1))
            elif token == '*':
                int1 = prev.pop()
                int2 = prev.pop()
                prev.append(int(int1) *  int(int2))
            else:
                prev.append(int(token))
        return math.floor(prev[0])