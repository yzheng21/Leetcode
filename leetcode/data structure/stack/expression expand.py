'''
1.split
2.recursion
3.concat
'''
class solution:
    def expressionexpand(self,str):
        stack = []
        num = ''
        for s in str:
            if s.isdigit():
                num += s
            elif s == '[':
                stack.append(int(num))
                num = ''
            elif s == ']':
                strings = []
                while stack:
                    top = stack.pop()
                    if type(top) == int:
                        stack.append(''.join(reversed(strings))*top)
                    else:
                        strings.append(top)
            else:
                stack.append(s)
        return ''.join(stack)


res = solution().expressionexpand('3[2[abc]]')
print(res)
