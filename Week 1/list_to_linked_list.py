class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def list_to_linked_list(self,arr):
        if not arr:
            return 
        node = Node(arr[0])
        self.head = node
        self.tail = node
        current = self.head
        
        for i in arr[1:]:
            new_node  = Node(i)
            current.next = new_node
            new_node.prev = current
            current = new_node
            
        self.tail = current
        
    def print_list(self):
        temp = self.tail
        
        if temp is None:
            return
        
        while temp:
            print(temp.data,end=" --> ")
            temp = temp.prev
        
        print("None")
        
arr = [1,2,3,4,5,6,7]
list1 = LinkedList()
list1.list_to_linked_list(arr)
list1.print_list()