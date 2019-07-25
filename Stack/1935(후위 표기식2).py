stack=[]
values=[]
n=int(input())
postfix=input()

for i in range(n):
    values.append(int(input()))
for i in postfix:
    if(64<ord(i)<91):
        stack.append(values[ord(i)-65])
    elif i=='+':
        a=stack.pop()
        b=stack.pop()
        stack.append(b+a)
    elif i=='-':
        a=stack.pop()
        b=stack.pop()
        stack.append(b-a)       
    elif i=='*':
        a=stack.pop()
        b=stack.pop()
        stack.append(b*a)
    elif i=='/':
        a=stack.pop()
        b=stack.pop()
        stack.append(b/a)
print(format(stack[0],'.2f'))
