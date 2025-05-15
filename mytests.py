def nextGreater(ls):
    stack = []
    ans = []
    for i in range(len(ls) - 1, -1, -1):
        while stack and stack[-1] <= ls[i]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(ls[i])
    ans.reverse()
    return ans

print(nextGreater([2,1,2,3,4]))