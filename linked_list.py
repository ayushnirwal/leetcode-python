class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert_at_end(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node

    def delete_node(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        if current.next:
            current.next = current.next.next

    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print('None')
        
    def create_from_array(self, arr):
        for val in arr:
            self.insert_at_end(val)

    def is_equal(self, other):
        current1, current2 = self.head, other.head
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None

