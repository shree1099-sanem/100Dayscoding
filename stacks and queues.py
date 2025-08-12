from pydoc_data.topics import topics


class Mystack:
    def __init__(self,capacity):
        self.stack=[0]*capacity
        self.top = -1
        self.capacity=capacity

    def push(self,element):
        if self.top == self.capacity-1:
            print('stack overflow')
            return
        self.top = self.top +1
        self.stack[self.top]=element

    def pop(self):
        if self.isempty():
            print('stack underflow')
            return -1
        element = self.stack[self.top]
        self.top = self.top -1
        return element

    def peek(self):
        if self.isempty():
            print("stack is empty, no top elements")
            return None
        return self.stack[self.top]

    def size(self):
        return self.top+1

    def display(self):
        if self.isempty():
            print("stack is empty")
        else:
            for i in range(self.top+1):
                print(self.stack[i])

    def isempty(self):
        return self.top == -1

s=Mystack(3)
s.push(100)
s.push(200)
s.push(300)
print("popped:",s.pop())
print("top element:",s.peek())
print("current size:",s.size())
s.display()


#queues
class Myqueue:
    def __init__(self,capacity):
        self.queue=[0]*capacity
        self.capacity=capacity
        self.front=0
        self.rear=0
        self.size=0

    def enqueue(self,element):
        if self.isfull()==True:
            print("queue is full")
            return -1
        self.queue[self.rear]=element
        self.rear = (self.rear+1)%self.capacity
        self.size += 1
        print(f" added {element} successfully")

    def dequeue(self):
        if self.isempty()==True:
            print("queue is empty")
            return -1
        element= self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f" removed {element} successfully")
        return element

    def current_size(self):
        return self.size

    def isfull(self):
        return self.size == self.capacity

    def isempty(self):
        return self.size==0

    def display(self):
        if self.isempty():
            print("queue is empty ")
            return
        print("queue contents:",end=" ")
        index=self.front
        for i in range(self.size):
            print(self.queue[index],end=" ")
            index= (index+1)% self.capacity
        print()

q=Myqueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
q.dequeue()
q.enqueue(60)
print(q.current_size())
q.display()

