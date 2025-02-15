from linked_list import LinkedList

def mergeTwoLists(list1,list2):
    result = LinkedList()

    head1 = list1
    head2 = list2

    print(head1)

    while head1.next == None:
        print(head1.value)
        head1 = head1.next

    # while marker1 < len(list1) and marker2 < len(list2):
    #     if list1[marker1] > list2[marker2]:
    #         result.append( list2[marker2] )
    #         marker2+=1
    #     else:
    #         result.append( list1[marker1] )
    #         marker1+=1
    
    # if marker1 < len(list1):
    #     result = result + list1[marker1:len(list1)]
    # if marker2 < len(list2):
    #     result = result + list2[marker2:len(list2)]


    return result

# def test_1():
#     list1 = LinkedList([1,2,4])
#     list2 = LinkedList([1,3,4])

#     result = LinkedList([1,1,2,3,4,4])

#     assert mergeTwoLists( list1, list2 ) == result

list1 = LinkedList([1,2,4])
list2 = LinkedList([1,3,4])

print(mergeTwoLists(list1,list2))


