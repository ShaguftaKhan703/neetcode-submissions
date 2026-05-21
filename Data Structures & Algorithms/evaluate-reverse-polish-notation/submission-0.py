class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        for token in tokens:

            match token:
                case "+":
                    a,b=stack.pop(),stack.pop()
                    stack.append(b+a)
                case "-":
                    a,b=stack.pop(),stack.pop()
                    stack.append(b-a)
                case "*":
                    a,b=stack.pop(),stack.pop()
                    stack.append(b*a)
                case "/":
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
                case _:
                    stack.append(int(token))
        return stack [0]
        