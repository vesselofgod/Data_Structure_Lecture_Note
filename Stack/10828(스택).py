N=int(input())
stack=[]
for i in range(N):
    com=input()
    if com[:4]=='push':
        stack.append(com[5:])
    elif com=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif com=='size':
        print(len(stack))
    elif com=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif com=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
