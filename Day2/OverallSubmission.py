class Node:
    def __init__(self, value):
        self.value = value
        self.link_node = None

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node
        

class Stack(): 
    def __init__(self):
        self.top_item = None
        self.size = 0
        self.limit = 1000

    def has_space(self):
        if self.limit > self.size:
            return True

    def is_empty(self):
        if self.size == 0:
            return True

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_link_node(self.top_item)
            self.top_item = item
            self.size = self.size+1
            return item
        else:
            print("All out of space!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_link_node()
            self.size = self.size-1
            return item_to_remove
        else:
            print("Empty Stack")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Empty Stack")

pizza_stack = Stack() 
pizza_stack.push("Pizza:1")
print(pizza_stack.peek())
pizza_stack.push("Pizza:2") 
print(pizza_stack.peek())
pizza_stack.push("Pizza:3")
print(pizza_stack.peek())
pizza_stack.pop()
print(pizza_stack.peek())
pizza_stack.pop()
print(pizza_stack.peek())
