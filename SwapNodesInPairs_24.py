# iteration: 虚拟头指针，双索引（游标），维护一个前驱节点
# recursion:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1. iteration, 维护一个前驱节点
        # 虚拟头指针技巧
        # dummy head node
        dummy = ListNode(-1)
        dummy.next = head
        # start swap
        prev = dummy
        # 当要交换的两个节点都存在时，执行交换
        while head and head.next:
            # 要交换的两个节点
            # i, j索引只是外壳，操作完成只需更新壳里的内容即可
            i = head
            j = i.next
            # swapping
            i.next = j.next
            j.next = i
            prev.next = j
            # update head
            prev = i
            head = i.next
        return dummy.next

        # # 2. recursion:
        # #
        # if head is None or head.next is None:
        #     return head
        # i = head
        # j = i.next
        # i.next = self.swapPairs(j.next)
        # j.next = head
        # return j

        # # 3. just swap value.  hack!
        # # dummy head node
        # dummy = ListNode(-1)
        # dummy.next = head
        # while head and head.next:
        #     tmp = head.val
        #     head.val = head.next.val
        #     head.next.val = tmp
        #     head = head.next.next
        # return dummy.next