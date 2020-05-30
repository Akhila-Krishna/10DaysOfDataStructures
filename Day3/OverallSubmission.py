class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, value = None):
        self.value = value
        self.head_node = self.value

    def get_head_node(self):
        return self.head_node 

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_value

    def stringify_list(self):
        node = Node(self.head_node)
        s = ""
        while node is not None:
            s = s + str(node.get_value())
            node = node.get_next_node()
        return s

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if self.head_node == value_to_remove:
            self.head_node = value_to_remove
        else:
            while current_node is not None:
                if current_node.get_next_node().get_value() == value_to_remove:
                    current_node.set_next_node(current_node.get_next_node()) 
                    current_node = None

# TASK 1
my_node = LinkedList()
my_node.insert_beginning(12)
my_node.insert_beginning(34)
print(my_node.get_head_node())
print(my_node.stringify_list())
