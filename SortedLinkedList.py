class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def merge_sorted_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.data < list2.data:
        list1.next = merge_sorted_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_sorted_lists(list1, list2.next)
        return list2

def print_linked_list_with_list(head):
    datas = []
    while head:
        datas.append(head.data)
        head = head.next
    print(" -> ".join(map(str, datas)))

def print_linked_lists_and_merged(list1, list2):
    print("List 1:")
    print_linked_list_with_list(list1)

    print("\nList 2:")
    print_linked_list_with_list(list2)

    merged_list = merge_sorted_lists(list1, list2)

    print("\nMerged List:")
    print_linked_list_with_list(merged_list)

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print_linked_lists_and_merged(list1, list2)