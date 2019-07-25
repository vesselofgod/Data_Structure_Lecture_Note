class SList:
    
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.next=link

    def __init__(self):
        self.head=None
        self.end=None
        self.size=0

    def size(self): return self.size
    def is_empty(self): return self.size==0

    def insert_front(self,item):
        if self.is_empty():
            n = self.Node(item,None)
            self.head=n
            self.end=n
        else:
            self.head=self.Node(item,self.head)
            
        self.size+=1

    def insert_end(self,item):
        self.end.next=self.Node(item, None)
        self.end=self.end.next
        self.size+=1
    
    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        
        elif(self.size==1):
            self.head=None
            self.size-=1
            
        else:
            self.head=self.head.next
            self.size-=1
            
    def pop_front(self):
        n=self.head
        self.delete_front()
        return n
    
    def rotate_left(self):
        p=self.head
        self.head=self.head.next
        self.insert_end(p.item)
        self.size-=1
        
    def rotate_right(self):
        p=self.end
        n=self.head
        while (n.next!=self.end):
            n=n.next
        self.end=n
        n.next=None
        self.insert_front(p.item)
        self.size-=1

    def search(self,target):
        p=self.head
        for k in range(self.size):
            if target==p.item: return k #탐색 성공
            p=p.next
        return None #탐색 실패

    def print_list(self):
        p = self.head
        while p:
            if p.next!=None:
                print(p.item,'->',end='')
            else:
                print(p.item)
            p=p.next
            
class EmptyError(Exception):
    pass

answer=0
N,M=map(int,input().split())
searchidx = list(map(int, input().split()))
LL=SList()
for i in range(N,0,-1):
    LL.insert_front(i)
    
for i in searchidx:
    count=0
    idx=LL.search(i)
    if (LL.size-idx > LL.size/2):#왼쪽으로 이동시키는 게 더 빠를 경우
        while LL.head.item!=i:
            LL.rotate_left()
            count+=1

    else:

        while LL.head.item!=i:
            LL.rotate_right()
            count+=1

    answer+=count
    LL.pop_front()

print(answer)
