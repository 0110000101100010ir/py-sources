
class Stack:
    def __init__(self):
        self.items = list()
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return(self.items == [])
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
 

def paren_check(var):
    p = Stack()
    
    open_set = "( { ["
    close_set = "] } )"
    match = ["()","{}","[]"]
    
    for item in var:
        if item in open_set.split():
            p.push(item)
        elif item in close_set.split() and p.is_empty():
            return "incomplete"
        elif item in close_set.split() and not p.is_empty():
            if (p.peek()+item) in match:
                p.pop()
            else:
                return "wrong order"
       
            
    if p.is_empty():
        return "complete"
    else:
        return "incomplete"
    
    
print(paren_check("[{(hi, this is parenthesis check, clumsy code! duh! )}]")) #complete

    
print(paren_check("{[(hi, this is parenthesis check, clumsy code! duh! )}]")) #wrong_order

    
print(paren_check("[{(hi, this is parenthesis check, clumsy code! duh! }]")) #incomplete but will result wrong_order :(
        
       
        
