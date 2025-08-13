class Stack: 
  def __init__(self, items = []): 
      self.items = list(items) 
       
  def pop(self): 
      self.items = self.items[1:] 
      return self.items 
       
  def push(self,item): 
      self.items = [item] + self.items 
      return self.items 
# stack = Stack([1,2,3,4,5]) 
while (1):
    c = int(input("enter the choice: "))
    if c == 1:
        prin
    elif c == 2:
        push()