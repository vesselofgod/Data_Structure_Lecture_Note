class Queue:
    front=(-1)
    back=(-1)
    item=[]
    
    def isEmpty(self):
        return self.back==-1

    def push(self, item):
        self.back+=1
        self.item.append(item)

    def pop(self):
        if self.isEmpty(): return -1
        self.back-=1
        value=self.item[0]
        del self.item[0]
        return value

    def d_front(self):
        if self.isEmpty(): return -1
        return self.item[0]
    def d_back(self):
        if self.isEmpty(): return -1
        return self.item[self.back]
    def size(self):
        if self.isEmpty(): return 0
        return self.back+1
