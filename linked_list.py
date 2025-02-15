class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data=None):
        self = None 

        if isinstance(data, list):
            for value in data:
                new_node = Node(data)

                if self is None:
                    self = new_node
                else:
                    current = self
                    while current.next:
                        current = current.next
                    current.next = new_node
