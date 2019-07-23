from listQueue import Queue

q=Queue()

n=int(input())

for i in range(n):
    command=input().split()
    if(command[0]=='push'):
        q.push(int(command[1]))
    if (command[0] == 'pop'):
        print(q.pop())
    if (command[0] == 'size'):
        print(q.size())
    if (command[0] == 'empty'):
        print(q.isEmpty())
    if (command[0] == 'front'):
        print(q.d_front())
    if (command[0] == 'back'):
        print(q.d_back())
