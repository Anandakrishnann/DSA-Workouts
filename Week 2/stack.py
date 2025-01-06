class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        print(f"data added{data}")
        
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
            
    def display(self):
        print(self.stack)
        
def reverse(data):
    stack = Stack()
    for i in data:
        stack.push(i)
    
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    
    return result

arr = "olleh"
res = reverse(arr)
print(res)
    

