class CList:
    class Node:
        def __init__(self,item,flink,nlink):
            self.item=item
            self.front=flink
            self.next=nlink
    def __init__(self):
        self.point=None
        self.size=0
    def isEmpty(self):
        return self.size==0
    def insert(self,item):
        n=self.Node(item,None,None)
        if self.isEmpty():
            n.next=n
            n.front=n
            self.point=n
        else:
            p=self.point.next
            n.next=self.point.next
            p.front=n
            self.point.next=n
            n.front=self.point
        self.size+=1
    def rotate_right(self):
        self.point=self.point.front
    def rotate_left(self):
        self.point=self.point.next
    def print_list(self):
        f=self.point
        p=f
        while p.front != f:
            print(p.item,end=',')
            p=p.front
        print(p.item)

    def delete(self):
        popValue=self.point
        p=self.point.next
        self.point=self.point.front
        p.front=self.point
        self.point.next=p
        self.size-=1
        return popValue
    
    def get_pointValue(self):
        return self.point.item
    def get_node(self,List):
        p=self.point
        f=p
        while p.front != f:
            List.append(p)
            p=p.front
        List.append(p)

N=int(input())
value=list(map(int,input().split()))
nodeList=[]
CLL=CList()
for i in range(N):
    CLL.insert(value[i])
CLL.get_node(nodeList)

result=[]
P_result=[]

for i in range(1,N+1):
    move=CLL.get_pointValue()-1
    pop=CLL.delete()
    subList=[pop,i]
    result.append(subList)
    if move>=0:  
        for j in range(abs(move)):
            CLL.rotate_right()

    else:
        for j in range(abs(move+1)):
            CLL.rotate_left()

for i in range(N):
    count=0
    while nodeList[count]!=result[i][0]:
        count+=1
    print(str(count+1)+' ', end='')
