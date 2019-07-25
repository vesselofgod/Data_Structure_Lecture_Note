class queue:
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.next=link

    def __init__(self):
        self.head=None
        self.end=None
        self.size=0

    def insert(self,item):
        n=self.Node(item,None)
        if self.size==0:
            self.head=n
            self.end=n
        else:
            self.end.next=n
            self.end=self.end.next
        self.size+=1
    def print_queue(self):
        p=self.head
        while (p!=None):
            print(p.item,'->',end='')
            p=p.next
        print()
    def delete(self):
        if(self.size>0):
            self.head=self.head.next
        self.size-=1
    def goBakc(self):
        n=self.head
        self.head=self.head.next
        self.end.next=n
        self.end=self.end.next

q=queue()
n=int(input())
for i in range(1,n+1):
    q.insert(i)
while(q.size!=1):
    q.delete()
    q.goBakc()

print(q.end.item)
