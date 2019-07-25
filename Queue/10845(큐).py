N=int(input())
queue=[]
for i in range(N):
    com=input()
    if com[:4]=='push':
        queue.append(com[5:])
    elif com=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif com=='size':
        print(len(queue))
    elif com=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif com=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])

    elif com=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
