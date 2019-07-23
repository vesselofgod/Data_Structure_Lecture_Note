from slist import SList

if __name__ =='__main__':
    s=SList()
    s.insert_front('orange')
    s.insert_front('apple')
    s.insert_after('cherry', s.head.next)
    s.insert_front('pear')
    s.print_list()
    print('cherry는 %d번째' % s.search('cherry'))

    print('pear 다음 노드 삭제 후 : ', end='')
    s.delete_after(s.head)
    s.print_list()

    print('첫 노드 삭제 후 : ',end='')
    s.delete_front()
    s.print_list()
    print('첫 노드로 망고, 딸기를 삽입한 후 : ',end='')
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()
    print('오렌지 다음 노드 삭제 후 : ',end='')
    s.delete_after(s.head.next.next)
    s.print_list()
