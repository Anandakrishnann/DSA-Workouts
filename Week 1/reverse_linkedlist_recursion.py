class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def list_to_linked_list(self,data):
        
        if not data:
            return
        
        node = Node(data[0])
        self.head = node
        self.tail = node
        current = self.head
        
        for i in data[1:]:
            new_node = Node(i)
            current.next = new_node
            new_node.prev = current
            current = new_node
            
        self.tail = current
        
    def reverse_recursion(self,node):
        
        if node is None or node.next is None:
            return node
        
        new_head = self.reverse_recursion(node.next)
        
        node.next.next = node
        node.next = None
        
        return new_head

    def reverse(self):
        self.head = self.reverse_recursion(self.head)
            
    def print_list(self):
        temp = self.head
        
        if temp is None:
            return
        
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
            
        print("None")
        
        
data = [1,2,3,4,5,6,7]
list1 = LinkedList()
list1.list_to_linked_list(data)
list1.print_list()
list1.reverse()
list1.print_list()