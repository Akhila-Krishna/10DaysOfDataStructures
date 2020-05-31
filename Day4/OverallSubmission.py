
# Check if the given input list is circular.
def is_circular_linked_list(self, input_list):
    pass
    if input_list.get_next_node() == None:
        return True
    next_node = head_node.get_next_node()
    while next_node != None and next_node != head_node:
        next_node = next_node.get_next_node()
    if next_node == head_node:
        return True
    return False