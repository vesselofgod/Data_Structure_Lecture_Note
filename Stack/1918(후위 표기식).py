stack=[]

infix=input()

for i in infix:
    if(64<ord(i)<91):
        print(i,end='')
    elif(i=='+' or i=='-'):
        while len(stack)>0:
            if (stack[-1]=='('):
                break
            print(stack.pop(),end='')
        stack.append(i)
    elif(i=='*' or i=='/'):
        while (len(stack)>0 and (stack[-1]=='*' or stack[-1]=='/')):
            if (stack[-1]=='('):
                break
            print(stack.pop(),end='')
        stack.append(i)
    elif(i=='('): stack.append(i)
    elif(i==')'):
        while True:
            ops=stack.pop()
            if ops=='(':
                break
            else:
                print(ops,end='')

for i in range(len(stack)):
    print(stack.pop(), end='')
