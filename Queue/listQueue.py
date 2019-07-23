class Queue:
    #큐 : 대기열과 같은 FIFO 구조(first in first out
    front=(-1) # 맨 앞 원소의 index를 의미함
    back=(-1)# 맨 뒤 원소의 index를 의미함
    item=[] 
    
    def isEmpty(self):
        return self.back==-1

    def push(self, item):
        self.back+=1#맨 뒤 원소의 idx 1 증가
        self.item.append(item)#맨 뒤부터 삽입되므로 append를 사용.

    def pop(self):
        if self.isEmpty(): return -1 #큐가 비어있을 경우 -1 리턴
        #큐에 원소가 들어 있을 경우 맨 앞의 원소를 지우고 반환하는 코드
        self.back-=1
        value=self.item[0]
        del self.item[0]
        return value

    def d_front(self):
        #맨 앞의 원소 반환하는 함수
        if self.isEmpty(): return -1
        return self.item[0]
    def d_back(self):
        #맨 뒤의 원소를 반환하는 함수
        if self.isEmpty(): return -1
        return self.item[self.back]
    def size(self):
        if self.isEmpty(): return 0
        return self.back+1
