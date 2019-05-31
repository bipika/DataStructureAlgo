class Queue:
    def __init__(self):
        self.queue = list()
        self.first = -1
        self.last = -1

    def enqueue(self,value):
        if self.first==-1:
            self.first+=1
        self.last=self.last+1
        self.queue.insert(self.last,value)

    def printing(self,queue):
        for i in self.queue:
            print(i)


queue=Queue()
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(1)
queue.enqueue(7)

queue.printing(queue)