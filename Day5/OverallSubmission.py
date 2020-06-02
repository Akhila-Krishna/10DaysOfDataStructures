# Remove duplicates from doubly linked lists.

def remove_duplicates(self):
    pass
    if (head_node == None or head_node.get_next_node() == None):
        return head_node

    ptr1 = head_node
    ptr2 = None

    while(ptr1 != None):
        ptr2 = ptr2.get_next_node()
        while(ptr2 != None):
            next_node = ptr2.get_value()
            if ptr1.get_value() == pt2.get_value():
                ptr2.set_next_node(next_node.get_next_node()) 
                ptr2 = None
            else:
                ptr2 = next_node

    return head_node