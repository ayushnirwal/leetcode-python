# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# 3217. Delete Nodes From Linked List Present in Array

from linked_list import LinkedList

def modifiedList(nums, LL:LinkedList):

    head = LL.head

    # find first element not in nums
    while head.next != None:
        if head.val in nums:
            head = head.next
        else: 
            break

    cur = head

    while cur.next != None:
        if cur.next.val in nums:
            cur.next = cur.next.next
        else:
            cur = cur.next
    

    LL.head = head
    LL.display()
    return LL



def test_1():
    l1 = LinkedList()
    l1.create_from_array([1,2,3,4,5])

    l2 = LinkedList()
    l2.create_from_array([4,5])
    assert l2.is_equal(modifiedList([1,2,3],l1))

def test_2():
    l1 = LinkedList()
    l1.create_from_array([1,2,1,2,1,2])

    l2 = LinkedList()
    l2.create_from_array([2,2,2])
    assert l2.is_equal(modifiedList([1],l1)) 

def test_3():
    l1 = LinkedList()
    l1.create_from_array([1,2,3,4])

    l2 = LinkedList()
    l2.create_from_array([1,2,3,4])
    assert l2.is_equal(modifiedList([5],l1))