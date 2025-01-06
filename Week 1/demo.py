class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
    
    def add_node_after(self,target,data):
        node = Node(data)
        temp = self.head
        
        while temp is not None and temp.data != target:
            temp = temp.next
        
        if temp is None:
            return 

        if temp == self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            node.next = temp.next
            temp.next.prev = node
            temp.next = node
            node.prev = temp
            
    def node_delete(self,data):
        temp = self.head
        
        if temp and temp.data == data and temp == self.head:
            
            if self.head == self.tail:
                self.head = None
                self.tail = None
                
            else:
                self.head = temp.next
                self.head.prev = None
        
        while temp is not None and temp.data != data:
            temp = temp.next
        
        if temp is None:
            return
        
        if temp == self.tail:
            self.tail = temp.prev
            self.tail.next = None
        
        if temp:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            
    def find_middle_element(self):
        
        f = self.head
        s = self.head
        
        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next
            
        if f:
            return s.data
        else:
            return None
        
    def print_list(self):
        head = self.head
        
        while head:
            print(head.data,end=" --> ")
            head = head.next
        print("None")
        
list1 = DoublyLinkedList()
list1.add_node(1)
list1.add_node(2)
list1.add_node(8)
list1.add_node(9)
list1.add_node(3)
list1.add_node(5)
list1.add_node_after(3,4)
list1.node_delete(8)
list1.node_delete(9)
m = list1.find_middle_element()
print(m)
list1.print_list()