class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.start=None


    def insert(self,value):
        if self.start==None:
            self.start=Node(value)
            return

        current= self.start

        while current.next is not None:
            current=current.next

        current.next=Node(value)

    def printing(self):
        current = self.start

        while current is not None:
            print(current.value)
            current = current.next

    def deleting(self,value):
        current =self.start
        print('after delete')
        while current is not None:
            if(current.value==value):
                if current.next==None:
                    current.value=None
                    return 
                current=current.next
            print(current.value)
            current = current.next

linkedlist=LinkedList()
linkedlist.insert(10)
linkedlist.insert(20)
linkedlist.insert(30)
linkedlist.insert(40)
linkedlist.insert(50)
linkedlist.printing()

linkedlist.deleting(50)