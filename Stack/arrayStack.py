class Stack:
    top=-1
    item=[]
    def isEmpty(self):
        return self.top==-1
    def push(self, item):
        self.top+=1
        self.item.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            self.top-=1
            return self.item.pop()#파이썬의 리스트에서 기본으로 지원함
    def size(self):
        return self.top+1
    def print_stack(self):
        for i in self.item:
            print(i,end=',')
        print()
