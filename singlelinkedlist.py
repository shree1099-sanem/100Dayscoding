class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Singlelinkedlinst:
    def __init__(self):
        self.root = None

    def AddNewNode(self, val):
        n = Node(val)
        if self.root == None:
            self.root = n
            return
        temp = self.root
        while temp.next != None:
            temp = temp.next
        temp.next = n

    def addbeginning(self,val):
        n=Node(val)
        if self.root == None:
            self.root = n
        n.next=self.root
        self.root=n

    def addafternth(self,val,pos):
        n=Node(val)
        temp=self.root
        count = 1
        while temp.next!=None and count<pos:
            temp=temp.next
            count += 1
        n.next=temp.next
        temp.next=n

    def deleteafternth(self,pos):
        count=1
        temp=self.root
        while temp.next!=None and count<pos:
            temp=temp.next
            count+=1
        temp.next=temp.next.next

    def display(self):
        temp=self.root
        while temp!=None:
            print(temp.val," ->",end=" ")
            temp=temp.next
        print("sll is empty")
sll=Singlelinkedlinst()
sll.AddNewNode(10)
sll.AddNewNode(20)
sll.AddNewNode(30)
sll.AddNewNode(40)
sll.addbeginning(5)
sll.addafternth(35,3)
sll.deleteafternth(4)
sll.display()




# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
# class Singlelinkedlinst:
#     def __init__(self):
#         self.root = None
#     def AddNewNode(self,val):
#         n=Node(val)
#         if self.root == None:
#             self.root=n
#             return
#         temp = self.root
#         while temp.next!=None:
#             temp = temp.next
#         temp.next=n
#     def display(self):
#         temp=self.root
#         while temp!=None:
#             print(temp.val," ->",end=" ")
#             temp=temp.next
#         print("sll is empty")
# sll=Singlelinkedlinst()
# sll.AddNewNode(10)
# sll.AddNewNode(20)
# sll.AddNewNode(30)
# sll.display()


