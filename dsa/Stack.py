class Stack:
    def  __init__(self):
        self.stack=list()

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack)<1:
            print ("Stack is empty")
        else:
            self.stack.pop()

    def printStack(self):
        print(self.stack)


stack=Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.printStack()
stack.pop()
stack.printStack()
stack.pop()
stack.printStack()
stack.pop()
stack.printStack()
stack.pop()
stack.printStack()