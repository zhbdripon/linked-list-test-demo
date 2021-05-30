class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        
    def get(self, index):
        cur_index = 0
        cur = self.head 
        while cur:
            if cur_index == index:
                return cur.data
            cur = cur.next
            cur_index+=1
        return -1

    def addAtHead(self, val):
        node = Node(val,self.head)
        self.head = node

    def addAtTail(self, val):
        if self.head is None:
            self.head = Node(val,None)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val,None)

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        cur_index = 0
        cur = self.head
        while cur:
            if cur_index + 1 == index:
                node = Node(val,cur.next)
                cur.next = node
                return
            cur = cur.next
            cur_index+=1
        
    def deleteAtIndex(self, index):
        cur_index = 0
        cur = self.head
        prv = None
        while cur:
            if cur_index == index:
                if prv is None:
                    self.head = cur.next
                elif cur.next is None:
                    prv.next = None
                else:
                    prv.next = cur.next
                return
            prv = cur
            cur = cur.next
            cur_index+=1

    def __str__(self):
        ret = ""
        if self.head is None:
            return "List is empty"
        else:
            cur = self.head
            while cur:
                ret += str(cur.data) + ' '
                cur = cur.next
        return ret

if __name__=="__main__":
    mylist = MyLinkedList()
    mylist.addAtHead(5)
    mylist.addAtHead(7)
    mylist.addAtTail(9)
    mylist.addAtTail(15)
    mylist.addAtIndex(0,99)
    print(mylist)
    print(mylist.get(0))
    mylist.deleteAtIndex(3)
    print(mylist)