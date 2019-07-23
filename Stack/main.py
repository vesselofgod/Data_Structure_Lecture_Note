from arrayStack import Stack

stack=Stack()

n=int(input())

for i in range(n):
    command=input().split()
    if(command[0]=='push'):
        stack.push(command[1])
    if (command[0] == 'pop'):
        print(stack.pop())
    if (command[0] == 'size'):
        print(stack.size())
    if (command[0] == 'empty'):
        print(stack.isEmpty())
    if (command[0] == 'print'):
        stack.print_stack()
