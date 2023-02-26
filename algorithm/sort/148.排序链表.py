# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def get_mid(head):

    # 对于偶数个元素的链表，first 一半，second 一半
    # 对于奇数个元素的链表，fisrt 比 second 多一个（所以实际上是右中位数）
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(first, second):

    dummy = ListNode(None)
    pre = dummy
    while first and second:
        if first.val < second.val:
            dummy.next = first
            first = first.next
        else:
            dummy.next = second
            second = second.next
        dummy = dummy.next
    if not first:
        dummy.next = second
    if not second:
        dummy.next = first
    return pre.next



class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next is None: # 不加这一行判断，会死循环。对于单个元素的输入，也是边界条件
            return head

        mid = get_mid(head)
        first, second = head, mid.next
        mid.next = None
        first, second = self.sortList(first), self.sortList(second) # 归并排序是先调用自己排好一半后，再归并
        res = merge(first, second)
        return res
